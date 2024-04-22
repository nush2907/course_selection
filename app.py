import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample list of courses with keywords
course_list = [
    {"course_name": "Strategic Financial Management", "keywords": ["financial management", "strategic planning", "financial analysis", "capital budgeting", "financial risk management"]},
    {"course_name": "Machine Learning for Time Series Analysis", "keywords": ["machine learning", "time series analysis", "forecasting", "feature engineering", "deep learning"]},
    {"course_name": "Data Science Fundamentals", "keywords": ["data science", "machine learning", "python", "statistics", "data analysis"]},
    {"course_name": "Web Development Bootcamp", "keywords": ["web development", "HTML", "CSS", "JavaScript", "frontend", "backend"]},
    {"course_name": "Digital Marketing Essentials", "keywords": ["digital marketing", "social media", "SEO", "content marketing", "online advertising"]},
    {"course_name": "Python Programming Basics", "keywords": ["python programming", "programming basics", "variables", "loops", "functions"]},
    {"course_name": "Financial Accounting Fundamentals", "keywords": ["financial accounting", "accounting basics", "balance sheet", "income statement", "financial ratios"]},
    {"course_name": "Mobile App Development with Flutter", "keywords": ["mobile app development", "flutter", "Dart", "UI design", "app deployment"]},
    {"course_name": "Business Analytics for Managers", "keywords": ["business analytics", "data-driven decision making", "analytics tools", "data visualization", "business intelligence"]},
    {"course_name": "Photography Masterclass", "keywords": ["photography", "camera settings", "composition", "lighting techniques", "post-processing"]},
    {"course_name": "Artificial Intelligence in Finance", "keywords": ["artificial intelligence", "finance", "machine learning", "algorithmic trading", "risk management"]},
    {"course_name": "UI/UX Design Principles", "keywords": ["UI/UX design", "user interface", "user experience", "design thinking", "prototyping"]},
    {"course_name": "Cybersecurity Fundamentals", "keywords": ["cybersecurity", "network security", "ethical hacking", "encryption", "security protocols"]},
    {"course_name": "Content Writing for the Web", "keywords": ["content writing", "SEO writing", "blogging", "copywriting", "content strategy"]},
    {"course_name": "Project Management Basics", "keywords": ["project management", "project planning", "team management", "risk management", "project lifecycle"]},
    {"course_name": "Social Psychology Fundamentals", "keywords": ["social psychology", "group dynamics", "social influence", "communication", "behavioral psychology"]},
    {"course_name": "E-commerce Business Strategies", "keywords": ["e-commerce", "online retail", "digital marketing", "customer acquisition", "e-commerce platforms"]},
    {"course_name": "Public Speaking Mastery", "keywords": ["public speaking", "presentation skills", "speech writing", "confidence building", "audience engagement"]},
    {"course_name": "Advanced Excel Techniques", "keywords": ["advanced excel", "data analysis", "macros", "pivot tables", "data visualization"]},
    {"course_name": "Leadership and Team Management", "keywords": ["leadership", "team management", "motivation techniques", "conflict resolution", "communication skills"]},
    {"course_name": "Blockchain Technology Fundamentals", "keywords": ["blockchain", "cryptocurrency", "smart contracts", "decentralized applications", "blockchain security"]},
    {"course_name": "Data Visualization with Tableau", "keywords": ["data visualization", "Tableau", "data analysis", "dashboard design", "business intelligence"]},
    {"course_name": "Healthcare Management Essentials", "keywords": ["healthcare management", "healthcare administration", "healthcare policy", "healthcare finance", "medical ethics"]},
    {"course_name": "Strategic Marketing Management", "keywords": ["strategic marketing", "marketing management", "market analysis", "brand management", "marketing strategy"]},
    {"course_name": "Game Development with Unity", "keywords": ["game development", "Unity", "C#", "game design", "game mechanics"]},
    {"course_name": "Machine Learning for Business", "keywords": ["machine learning", "business analytics", "predictive modeling", "data-driven decision making", "business intelligence"]},
    {"course_name": "Digital Illustration Techniques", "keywords": ["digital illustration", "Adobe Illustrator", "vector graphics", "drawing techniques", "graphic design"]},
    {"course_name": "Human Resources Management Fundamentals", "keywords": ["human resources management", "employee relations", "recruitment", "training and development", "performance management"]},
    {"course_name": "Financial Management Principles", "keywords": ["financial management", "budgeting", "financial analysis", "investment strategies", "risk management"]},
    {"course_name": "English Language Proficiency", "keywords": ["English language", "grammar", "vocabulary", "reading comprehension", "writing skills"]},
    {"course_name": "Artificial Intelligence Fundamentals", "keywords": ["artificial intelligence", "machine learning", "deep learning", "natural language processing", "neural networks"]},
    {"course_name": "Business Process Improvement", "keywords": ["business process improvement", "process optimization", "lean six sigma", "continuous improvement", "process mapping"]},
    {"course_name": "Data Engineering Basics", "keywords": ["data engineering", "ETL processes", "data modeling", "big data technologies", "database management"]},
    {"course_name": "Brand Management Strategies", "keywords": ["brand management", "brand strategy", "brand positioning", "brand identity", "brand equity"]},
    {"course_name": "Advanced Data Analysis Techniques", "keywords": ["data analysis", "statistical analysis", "predictive modeling", "data mining", "machine learning algorithms"]},
    {"course_name": "Computer Networking Fundamentals", "keywords": ["computer networking", "network architecture", "routing protocols", "network security", "TCP/IP"]},
    {"course_name": "Database Management Essentials", "keywords": ["database management", "SQL", "database design", "data modeling", "database administration"]},
    {"course_name": "Human Resources Management", "keywords": ["human resources management", "recruitment", "employee relations", "performance management", "training and development"]},
    {"course_name": "Content Writing Skills", "keywords": ["content writing", "copywriting", "SEO writing", "creative writing", "research skills"]},
    {"course_name": "Computer Programming Logic", "keywords": ["programming logic", "algorithmic thinking", "problem solving", "code optimization", "flowcharting"]},
    {"course_name": "Social Media Management", "keywords": ["social media management", "content creation", "audience engagement", "social media analytics", "community management"]},
    {"course_name": "Data Visualization Techniques", "keywords": ["data visualization", "data interpretation", "visualization tools", "dashboard design", "storytelling with data"]},
    {"course_name": "Software Testing Fundamentals", "keywords": ["software testing", "test planning", "test case design", "defect management", "automation testing"]},
    {"course_name": "User Interface Design Principles", "keywords": ["user interface design", "UI design principles", "wireframing", "prototyping", "user research"]},
    {"course_name": "Fundamentals of Cloud Computing", "keywords": ["cloud computing", "cloud service models", "virtualization", "cloud security", "AWS"]},
    {"course_name": "Mobile App UI/UX Design", "keywords": ["mobile app UI/UX design", "mobile design guidelines", "prototyping tools", "user-centered design", "mobile app usability"]},
    {"course_name": "Business Analytics Fundamentals", "keywords": ["business analytics", "data analysis", "data visualization", "predictive analytics", "statistical modeling"]},
    {"course_name": "Ethical Hacking and Penetration Testing", "keywords": ["ethical hacking", "penetration testing", "network security", "web application security", "vulnerability assessment"]},
    {"course_name": "English Language Writing Skills", "keywords": ["English language", "writing skills", "grammar", "vocabulary", "creative writing"]},
    {"course_name": "Financial Accounting Basics", "keywords": ["financial accounting", "accounting principles", "financial statements", "bookkeeping", "financial analysis"]},
    {"course_name": "Machine Learning with Python", "keywords": ["machine learning", "python programming", "data preprocessing", "supervised learning", "unsupervised learning"]},
    {"course_name": "Java Web Development", "keywords": ["Java", "web development", "Servlets", "JSP", "Spring Framework"]},
    {"course_name": "Creative Problem Solving Techniques", "keywords": ["creative problem solving", "brainstorming", "design thinking", "critical thinking", "innovation"]},
    {"course_name": "Marketing Analytics Fundamentals", "keywords": ["marketing analytics", "data analysis", "marketing strategy", "customer segmentation", "predictive modeling"]},
    {"course_name": "JavaScript Frameworks", "keywords": ["JavaScript", "React", "Angular", "Vue.js", "frontend development"]},
    {"course_name": "Leadership Skills Development", "keywords": ["leadership", "team management", "communication skills", "decision making", "conflict resolution"]},
    {"course_name": "Data Engineering Fundamentals", "keywords": ["data engineering", "ETL processes", "data warehousing", "big data technologies", "data pipeline development"]},
    {"course_name": "Human-Centered Design", "keywords": ["human-centered design", "user-centered design", "empathy mapping", "prototyping", "user testing"]},
    {"course_name": "Game Design Principles", "keywords": ["game design", "game mechanics", "level design", "game balancing", "user engagement"]},
    {"course_name": "Strategic Management Fundamentals", "keywords": ["strategic management", "strategic planning", "SWOT analysis", "competitive analysis", "business model canvas"]},
    {"course_name": "Technical Writing Skills", "keywords": ["technical writing", "documentation", "technical communication", "writing style", "editing"]},
    {"course_name": "Database Administration Basics", "keywords": ["database administration", "database management systems", "SQL", "backup and recovery", "performance tuning"]},
    {"course_name": "Business Process Improvement", "keywords": ["business process improvement", "process mapping", "lean six sigma", "continuous improvement", "root cause analysis"]},
    {"course_name": "Digital Illustration Techniques", "keywords": ["digital illustration", "Adobe Illustrator", "vector graphics", "drawing techniques", "color theory"]},
    {"course_name": "Cloud Computing Security", "keywords": ["cloud computing", "cloud security", "identity and access management", "encryption", "compliance"]},
    {"course_name": "Social Psychology Fundamentals", "keywords": ["social psychology", "group dynamics", "social influence", "interpersonal communication", "cognitive biases"]},
    {"course_name": "Business Communication Skills", "keywords": ["business communication", "email etiquette", "negotiation skills", "presentation skills", "effective meetings"]},
    {"course_name": "Healthcare Management Fundamentals", "keywords": ["healthcare management", "healthcare administration", "health policy", "quality improvement", "healthcare finance"]},
    {"course_name": "iOS App Development with Swift", "keywords": ["iOS app development", "Swift", "Xcode", "user interface design", "app deployment"]},
    {"course_name": "Game Engine Architecture", "keywords": ["game engine development", "graphics programming", "physics simulation", "rendering techniques", "game engine optimization"]},
    {"course_name": "Supply Chain Management Basics", "keywords": ["supply chain management", "logistics", "inventory management", "procurement", "demand forecasting"]},
    {"course_name": "Brand Management Strategies", "keywords": ["brand management", "brand strategy", "brand positioning", "brand identity", "brand equity"]},
    {"course_name": "Cloud Native Application Development", "keywords": ["cloud native", "microservices architecture", "containers", "Kubernetes", "serverless computing"]},
    {"course_name": "Agile Project Management", "keywords": ["agile methodology", "Scrum", "Kanban", "sprint planning", "user stories"]},
    {"course_name": "Advanced Data Analysis Techniques", "keywords": ["data analysis", "advanced statistics", "predictive modeling", "data mining", "time series analysis"]},
    {"course_name": "Machine Learning for Business", "keywords": ["machine learning", "business analytics", "predictive modeling", "data visualization", "decision support systems"]},
    {"course_name": "Android App Development with Kotlin", "keywords": ["Android app development", "Kotlin", "Android Studio", "user interface design", "app deployment"]},
    {"course_name": "Network Security Fundamentals", "keywords": ["network security", "firewalls", "intrusion detection systems", "cryptography", "VPN"]},
    {"course_name": "Professional Email Writing Skills", "keywords": ["email writing", "professional communication", "business writing", "email etiquette", "writing tone"]},
    {"course_name": "Business Strategy Development", "keywords": ["business strategy", "strategic planning", "competitive analysis", "market research", "SWOT analysis"]},
    {"course_name": "Content Strategy and Marketing", "keywords": ["content strategy", "content marketing", "content creation", "audience analysis", "content distribution"]},
    {"course_name": "iOS App UI/UX Design", "keywords": ["iOS app UI/UX design", "human interface guidelines", "prototyping tools", "user-centered design", "mobile app usability"]},
    {"course_name": "Quantitative Data Analysis", "keywords": ["quantitative data analysis", "statistical analysis", "data interpretation", "hypothesis testing", "regression analysis"]},
    {"course_name": "IT Project Management", "keywords": ["IT project management", "project planning", "scope management", "risk management", "resource allocation"]},
    {"course_name": "Copywriting for Digital Media", "keywords": ["copywriting", "content writing", "SEO writing", "content strategy", "persuasive writing"]},
    {"course_name": "Data Warehousing Concepts", "keywords": ["data warehousing", "data modeling", "ETL processes", "data integration", "data warehouse design"]},
    {"course_name": "Strategic Brand Management", "keywords": ["brand management", "brand strategy", "brand positioning", "brand equity", "brand identity"]},
    {"course_name": "Ethical Leadership and Decision Making", "keywords": ["ethical leadership", "decision making", "ethical decision making", "leadership ethics", "corporate social responsibility"]},
    {"course_name": "Agile Software Development", "keywords": ["agile methodology", "Scrum", "Kanban", "sprint planning", "user stories"]},
    {"course_name": "Consumer Behavior Analysis", "keywords": ["consumer behavior", "market research", "consumer psychology", "purchase decision making", "brand perception"]},
    {"course_name": "IoT Fundamentals", "keywords": ["Internet of Things (IoT)", "IoT devices", "sensor networks", "IoT applications", "IoT security"]},
    {"course_name": "Business Process Automation", "keywords": ["business process automation", "process analysis", "workflow automation", "RPA", "business process management"]},
    {"course_name": "User Experience Research", "keywords": ["user experience research", "user interviews", "usability testing", "persona development", "user journey mapping"]},
    {"course_name": "Data Governance Fundamentals", "keywords": ["data governance", "data management", "data quality", "data stewardship", "regulatory compliance"]},
    {"course_name": "Strategic Human Resources Management", "keywords": ["human resources management", "strategic planning", "talent management", "performance management", "employee engagement"]},
    {"course_name": "Web Application Security", "keywords": ["web application security", "OWASP Top 10", "vulnerability assessment", "penetration testing", "security best practices"]},
    {"course_name": "Leadership and Team Management", "keywords": ["leadership", "team management", "motivation techniques", "conflict resolution", "effective communication"]},
    {"course_name": "Content Management Systems", "keywords": ["content management systems", "CMS customization", "content publishing", "website management", "content workflow"]},
    {"course_name": "Business Intelligence Fundamentals", "keywords": ["business intelligence", "data warehousing", "data visualization", "data analysis", "dashboard design"]},
    {"course_name": "Data Mining Techniques", "keywords": ["data mining", "association rule mining", "classification", "clustering", "anomaly detection"]},
    {"course_name": "Organizational Behavior and Leadership", "keywords": ["organizational behavior", "leadership", "motivation", "team dynamics", "conflict resolution"]},
    {"course_name": "Digital Strategy and Transformation", "keywords": ["digital strategy", "digital transformation", "digital marketing", "customer experience", "innovation"]},
    {"course_name": "Cloud Infrastructure Management", "keywords": ["cloud infrastructure", "cloud migration", "cost management", "monitoring and optimization", "cloud security"]},
    {"course_name": "Business Process Reengineering", "keywords": ["business process reengineering", "process analysis", "process redesign", "change management", "workflow automation"]},
    {"course_name": "Project Risk Management", "keywords": ["project risk management", "risk identification", "risk assessment", "risk mitigation", "risk monitoring"]},
    {"course_name": "Advanced Excel Skills", "keywords": ["excel", "advanced formulas", "pivot tables", "charts and graphs", "macros"]},
    {"course_name": "Business Analytics with Python", "keywords": ["business analytics", "python programming", "data analysis", "data visualization", "predictive modeling"]},
    {"course_name": "Social Media Advertising Strategies", "keywords": ["social media advertising", "Facebook ads", "Instagram ads", "LinkedIn ads", "Twitter ads"]},
    {"course_name": "E-commerce Business Essentials", "keywords": ["e-commerce", "online store development", "digital marketing", "customer acquisition", "order fulfillment"]},
    {"course_name": "Machine Learning for Natural Language Processing", "keywords": ["machine learning", "natural language processing", "text mining", "sentiment analysis", "named entity recognition"]},
    {"course_name": "Digital Marketing Analytics", "keywords": ["digital marketing analytics", "Google Analytics", "social media analytics", "web traffic analysis", "conversion rate optimization"]},
    {"course_name": "Advanced Web Development", "keywords": ["advanced web development", "React.js", "Node.js", "RESTful APIs", "web security"]},
    {"course_name": "Supply Chain Analytics", "keywords": ["supply chain management", "data analysis", "data visualization", "supply chain optimization", "forecasting"]},
    {"course_name": "Strategic Financial Management", "keywords": ["financial management", "strategic planning", "financial analysis", "capital budgeting", "financial risk management"]},
    {"course_name": "Machine Learning for Time Series Analysis", "keywords": ["machine learning", "time series analysis", "forecasting", "feature engineering", "deep learning"]},
    {"course_name": "Business Ethics and Corporate Governance", "keywords": ["business ethics", "corporate governance", "ethical decision making", "corporate social responsibility", "legal compliance"]},
    {"course_name": "Advanced Database Management", "keywords": ["database management", "database administration", "SQL", "data modeling", "performance tuning"]},
]

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdf_file as f:
        pdf_reader = PdfReader(f)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to find keywords
def find_keywords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word.casefold() not in stop_words]
    return filtered_text

# Function to filter courses based on keywords
def filter_courses_by_keywords(keywords):
    suggested_courses = []
    max_matches = 0
    for course in course_list:
        course_keywords = course['keywords']
        match_count = sum(keyword.lower() in course_keywords for keyword in keywords)
        if match_count > 0:
            if len(suggested_courses) < 7:
                suggested_courses.append((course['course_name'], match_count))
                if match_count > max_matches:
                    max_matches = match_count
            else:
                suggested_courses.sort(key=lambda x: x[1], reverse=True)
                if match_count > suggested_courses[6][1]:
                    suggested_courses.pop()
                    suggested_courses.append((course['course_name'], match_count))
    suggested_courses.sort(key=lambda x: x[1], reverse=True)
    return [course[0] for course in suggested_courses]
def main():
    st.title("Course Recommendation based on Resume")
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

    if uploaded_file is not None:
        # Extract text from the uploaded PDF
        text = extract_text_from_pdf(uploaded_file)

        # Find keywords in the extracted text
        keywords = find_keywords(text)

        # Filter courses based on keywords
        suggested_courses = filter_courses_by_keywords(keywords)

        # Display suggested courses
        if suggested_courses:
            st.write("Suggested Courses based on your resume:")
            for course in suggested_courses:
                st.write(f"- {course}")
        else:
            st.write("No courses found based on your resume.")
        data = "Hello, World!"
        button_clicked = st.button("Check University")
        if button_clicked:
            st.write("Data:", data)
        
if __name__ == "__main__":
    main()
