import streamlit as st
from PyPDF2 import PdfReader
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
course_list = [
    {"course_name": "Data Science Fundamentals", "keywords": ["data science", "machine learning", "python"], "university": "TechHub University"},
    {"course_name": "Web Development Bootcamp", "keywords": ["web development", "HTML", "CSS", "JavaScript"], "university": "CodeMaster Institute"},
    {"course_name": "Digital Marketing Essentials", "keywords": ["digital marketing", "social media", "SEO"], "university": "MarketPro Academy"},
    {"course_name": "Software Engineering Principles", "keywords": ["software engineering", "programming", "software design"], "university": "CodeCraft University"},
    {"course_name": "Finance for Non-Finance Professionals", "keywords": ["finance", "accounting", "financial analysis"], "university": "MoneyMatters Institute"},
    {"course_name": "Cybersecurity Fundamentals", "keywords": ["cybersecurity", "network security", "information security"], "university": "SecureNet Academy"},
    {"course_name": "Business Analytics Masterclass", "keywords": ["business analytics", "data analysis", "predictive modeling"], "university": "BizTech School"},
    {"course_name": "Graphic Design Essentials", "keywords": ["graphic design", "Adobe Photoshop", "illustration"], "university": "DesignPro College"},
    {"course_name": "Leadership and Management Skills", "keywords": ["leadership", "management", "team building"], "university": "LeadWell University"},
    {"course_name": "Mobile App Development Bootcamp", "keywords": ["mobile app development", "iOS", "Android", "app design"], "university": "AppDev Institute"},
    {"course_name": "Project Management Fundamentals", "keywords": ["project management", "project planning", "agile methodology"], "university": "ProjectPro School"},
    {"course_name": "Artificial Intelligence Basics", "keywords": ["artificial intelligence", "machine learning", "neural networks"], "university": "AI Academy"},
    {"course_name": "Content Writing for Digital Media", "keywords": ["content writing", "copywriting", "SEO writing"], "university": "ContentCraft Institute"},
    {"course_name": "Healthcare Administration Essentials", "keywords": ["healthcare administration", "healthcare management", "health policy"], "university": "HealthPro University"},
    {"course_name": "Entrepreneurship and Startup Management", "keywords": ["entrepreneurship", "startup", "business development"], "university": "StartupLaunch College"},
    {"course_name": "Data Visualization Techniques", "keywords": ["data visualization", "infographics", "dashboard design"], "university": "VisualInsight Institute"},
    {"course_name": "Networking Fundamentals", "keywords": ["networking", "TCP/IP", "routing"], "university": "NetConnect Academy"},
    {"course_name": "Game Development Fundamentals", "keywords": ["game development", "Unity", "game design"], "university": "GameForge School"},
    {"course_name": "Human Resources Management Essentials", "keywords": ["human resources", "HR management", "recruitment"], "university": "HRPro College"},
    {"course_name": "Ethical Hacking and Penetration Testing", "keywords": ["ethical hacking", "penetration testing", "cybersecurity"], "university": "HackSafe Institute"},
    {"course_name": "Digital Photography Masterclass", "keywords": ["digital photography", "photography techniques", "Adobe Lightroom"], "university": "PhotoPro Academy"},
    {"course_name": "Supply Chain Management Principles", "keywords": ["supply chain management", "logistics", "inventory management"], "university": "SupplyLink College"},
    {"course_name": "UI/UX Design Essentials", "keywords": ["UI/UX design", "user interface design", "user experience"], "university": "DesignTech Institute"},
    {"course_name": "Blockchain Technology Basics", "keywords": ["blockchain", "cryptocurrency", "smart contracts"], "university": "ChainTech School"},
    {"course_name": "Advanced Excel Skills", "keywords": ["Excel", "data analysis", "pivot tables"], "university": "ExcelPro Institute"},
    {"course_name": "Presentation Skills Mastery", "keywords": ["presentation skills", "public speaking", "confidence building"], "university": "SpeakUp Academy"},
    {"course_name": "Digital Illustration Techniques", "keywords": ["digital illustration", "Adobe Illustrator", "vector graphics"], "university": "IllustrateIt Institute"},
    {"course_name": "Marketing Strategy Fundamentals", "keywords": ["marketing strategy", "branding", "market research"], "university": "MarketMasters School"},
    {"course_name": "Business Intelligence Essentials", "keywords": ["business intelligence", "data warehousing", "BI tools"], "university": "DataInsight College"},
    {"course_name": "Data Mining Fundamentals", "keywords": ["data mining", "data analysis", "pattern recognition"], "university": "MineData Institute"},
    {"course_name": "Creative Writing Workshop", "keywords": ["creative writing", "storytelling", "writing techniques"], "university": "WriteCraft Academy"},
    {"course_name": "Cloud Computing Fundamentals", "keywords": ["cloud computing", "AWS", "Azure", "virtualization"], "university": "CloudTech School"},
    {"course_name": "Customer Service Excellence", "keywords": ["customer service", "customer satisfaction", "communication skills"], "university": "ServicePro College"},
    {"course_name": "Data Warehousing Concepts", "keywords": ["data warehousing", "ETL processes", "data integration"], "university": "DataWare College"},
    {"course_name": "UX Research and Usability Testing", "keywords": ["UX research", "usability testing", "user interviews"], "university": "UXPro Institute"},
    {"course_name": "Financial Modeling Fundamentals", "keywords": ["financial modeling", "valuation", "forecasting"], "university": "FinancePro College"},
    {"course_name": "Mobile Marketing Strategies", "keywords": ["mobile marketing", "app advertising", "app monetization"], "university": "MobileMasters School"},
    {"course_name": "Social Media Management Essentials", "keywords": ["social media management", "content scheduling", "community engagement"], "university": "SocialPro Institute"},
    {"course_name": "Business Process Reengineering", "keywords": ["business process reengineering", "process optimization", "business transformation"], "university": "ProcessPro College"},
    {"course_name": "Machine Learning for Business", "keywords": ["machine learning", "business analytics", "predictive modeling"], "university": "ML4Biz School"},
    {"course_name": "Public Relations Fundamentals", "keywords": ["public relations", "media relations", "crisis management"], "university": "PRPro Institute"},
    {"course_name": "Risk Management Essentials", "keywords": ["risk management", "risk assessment", "risk mitigation"], "university": "RiskPro College"},
    {"course_name": "Video Production Techniques", "keywords": ["video production", "video editing", "cinematography"], "university": "VideoCraft Institute"},
    {"course_name": "Network Security Principles", "keywords": ["network security", "firewalls", "encryption"], "university": "SecureNet College"},
    {"course_name": "Business Negotiation Skills", "keywords": ["negotiation skills", "conflict resolution", "persuasion techniques"], "university": "NegotiateWell School"},
    {"course_name": "Database Management Essentials", "keywords": ["database management", "SQL", "database design"], "university": "DataTech Institute"},
    {"course_name": "Agile Project Management", "keywords": ["agile project management", "scrum", "sprint planning"], "university": "AgilePro College"},
    {"course_name": "Content Strategy and Marketing", "keywords": ["content strategy", "content marketing", "content creation"], "university": "ContentPro Institute"},
    {"course_name": "Mobile App UI/UX Design", "keywords": ["mobile app design", "UI/UX design", "mobile usability"], "university": "AppDesign College"},
    {"course_name": "Strategic Planning and Execution", "keywords": ["strategic planning", "business strategy", "strategic management"], "university": "StrategyPro School"},
    {"course_name": "Cloud Security Fundamentals", "keywords": ["cloud security", "security best practices", "identity management"], "university": "SecureCloud Institute"},
    {"course_name": "Email Marketing Essentials", "keywords": ["email marketing", "email automation", "email campaigns"], "university": "EmailPro College"},
    {"course_name": "Digital Advertising Strategies", "keywords": ["digital advertising", "online advertising", "PPC"], "university": "AdvertiseTech School"},
    {"course_name": "Strategic Brand Management", "keywords": ["brand management", "brand strategy", "brand positioning"], "university": "BrandPro Institute"},
    {"course_name": "Data Governance Fundamentals", "keywords": ["data governance", "data management", "data policies"], "university": "DataGov College"},
    {"course_name": "Leadership Development Program", "keywords": ["leadership development", "leadership skills", "leadership coaching"], "university": "LeadPro School"},
    {"course_name": "Social Psychology Essentials", "keywords": ["social psychology", "group behavior", "social influence"], "university": "SocialPsych Institute"},
    {"course_name": "Retail Management Fundamentals", "keywords": ["retail management", "merchandising", "inventory control"], "university": "RetailPro College"},
    {"course_name": "Mobile Game Development", "keywords": ["mobile game development", "game design", "game programming"], "university": "GameDev Institute"},
    {"course_name": "Operations Management Basics", "keywords": ["operations management", "process improvement", "quality management"], "university": "OpsPro School"},
    {"course_name": "Search Engine Optimization (SEO)", "keywords": ["search engine optimization", "SEO techniques", "keyword research"], "university": "SEOPro Institute"},
    {"course_name": "Strategic Financial Management", "keywords": ["financial management", "corporate finance", "financial analysis"], "university": "FinanceStrat College"},
    {"course_name": "Data Analysis with R Programming", "keywords": ["data analysis", "R programming", "data visualization"], "university": "DataR School"},
    {"course_name": "Brand Identity Design", "keywords": ["brand identity", "logo design", "brand guidelines"], "university": "BrandDesign Institute"},
    {"course_name": "Customer Relationship Management (CRM)", "keywords": ["CRM", "customer relationship", "sales management"], "university": "CRMPro School"},
    {"course_name": "Entrepreneurial Finance Fundamentals", "keywords": ["entrepreneurial finance", "startup funding", "venture capital"], "university": "StartupFinance College"},
    {"course_name": "Data Ethics and Privacy", "keywords": ["data ethics", "privacy laws", "ethical data practices"], "university": "DataEthics Institute"},
    {"course_name": "Strategic Marketing Management", "keywords": ["strategic marketing", "marketing planning", "brand management"], "university": "MarketStrat School"},
    {"course_name": "Machine Learning for Natural Language Processing", "keywords": ["machine learning", "natural language processing", "text mining"], "university": "NLP4ML Institute"},
    {"course_name": "Digital Transformation Strategies", "keywords": ["digital transformation", "business innovation", "change management"], "university": "DigitalTrans Institute"},
    {"course_name": "Business Process Automation", "keywords": ["business process automation", "workflow automation", "RPA"], "university": "ProcessAuto School"},
    {"course_name": "Marketing Analytics Essentials", "keywords": ["marketing analytics", "data analysis", "marketing ROI"], "university": "MarketingAnal School"},
    {"course_name": "Strategic Human Resources Management", "keywords": ["human resources management", "talent management", "HR strategy"], "university": "HRStrat Institute"},
    {"course_name": "Web Development with Python", "keywords": ["web development", "Python", "Django"], "university": "PythonWeb College"},
    {"course_name": "Business Process Improvement", "keywords": ["business process improvement", "process optimization", "continuous improvement"], "university": "BizImprovement Institute"},
    {"course_name": "Digital Product Management", "keywords": ["product management", "digital products", "product strategy"], "university": "ProdMgmt School"},
    {"course_name": "IT Service Management Essentials", "keywords": ["IT service management", "ITIL", "service desk"], "university": "ITService College"},
    {"course_name": "Advanced Networking Concepts", "keywords": ["networking", "advanced routing", "network protocols"], "university": "NetAdv School"},
    {"course_name": "Business Law Fundamentals", "keywords": ["business law", "legal regulations", "contracts"], "university": "LawBiz School"},
    {"course_name": "Data Visualization with Tableau", "keywords": ["data visualization", "Tableau", "data dashboards"], "university": "TableauViz Institute"},
    {"course_name": "Digital Content Creation", "keywords": ["digital content", "content creation", "multimedia production"], "university": "DigitalContent School"},
    {"course_name": "Strategic Management Principles", "keywords": ["strategic management", "business strategy", "strategic planning"], "university": "StratMgmt Institute"},
    {"course_name": "Ethical Leadership and Decision Making", "keywords": ["ethical leadership", "decision making", "integrity"], "university": "EthicalLead College"},
    {"course_name": "Fundamentals of Product Design", "keywords": ["product design", "design thinking", "prototyping"], "university": "ProdDesign School"},
    {"course_name": "Digital Entrepreneurship", "keywords": ["digital entrepreneurship", "online business", "startup strategies"], "university": "DigitalEntre School"},
    {"course_name": "Marketing Automation Fundamentals", "keywords": ["marketing automation", "email automation", "lead nurturing"], "university": "AutoMkt School"},
    {"course_name": "Data Analysis with Excel", "keywords": ["data analysis", "Excel", "data visualization"], "university": "ExcelAnal Institute"},
    {"course_name": "Strategic Branding and Identity", "keywords": ["strategic branding", "brand identity", "brand positioning"], "university": "BrandStrat School"},
    {"course_name": "Social Media Strategy Development", "keywords": ["social media strategy", "content planning", "engagement tactics"], "university": "SocMediaStrat College"},
    {"course_name": "Advanced Web Development Techniques", "keywords": ["web development", "advanced JavaScript", "full-stack development"], "university": "AdvWebDev Institute"},
    {"course_name": "Project Risk Management", "keywords": ["project risk management", "risk assessment", "risk mitigation"], "university": "RiskMgmt College"},
    {"course_name": "Data Analysis with Python", "keywords": ["data analysis", "Python", "data manipulation"], "university": "PythonAnal Institute"},
    {"course_name": "Strategic Innovation Management", "keywords": ["strategic innovation", "innovation strategy", "design thinking"], "university": "InnovationMgmt College"},
    {"course_name": "Digital Marketing Analytics", "keywords": ["digital marketing analytics", "marketing metrics", "data-driven marketing"], "university": "DigitalMktAnal Institute"},
    {"course_name": "Cloud Architecture and Design", "keywords": ["cloud architecture", "cloud services", "scalability"], "university": "CloudArch Institute"},
    {"course_name": "Strategic Sales Management", "keywords": ["strategic sales", "sales planning", "sales strategies"], "university": "SalesStrat College"},
    {"course_name": "Data Science for Business Analytics", "keywords": ["data science", "business analytics", "predictive modeling"], "university": "DS4Biz Institute"},
    {"course_name": "Digital Media Planning and Buying", "keywords": ["media planning", "media buying", "digital advertising"], "university": "MediaPlan Institute"},
    {"course_name": "Blockchain Applications and Use Cases", "keywords": ["blockchain applications", "blockchain use cases", "cryptocurrency"], "university": "BlockApp Institute"},
    {"course_name": "Strategic Project Management", "keywords": ["strategic project management", "project planning", "project execution"], "university": "ProjectStrat College"},
    {"course_name": "Data Visualization with Python", "keywords": ["data visualization", "Python", "matplotlib"], "university": "PythonViz Institute"},
    {"course_name": "Strategic Human Resources Management", "keywords": ["human resources management", "talent management", "HR strategy"], "university": "HRStrat Institute"},
    {"course_name": "Web Development with Python", "keywords": ["web development", "Python", "Django"], "university": "PythonWeb College"},
    {"course_name": "Business Process Improvement", "keywords": ["business process improvement", "process optimization", "continuous improvement"], "university": "BizImprovement Institute"},
    {"course_name": "Digital Product Management", "keywords": ["product management", "digital products", "product strategy"], "university": "ProdMgmt School"},
    {"course_name": "IT Service Management Essentials", "keywords": ["IT service management", "ITIL", "service desk"], "university": "ITService College"},
    {"course_name": "Advanced Networking Concepts", "keywords": ["networking", "advanced routing", "network protocols"], "university": "NetAdv School"},
    {"course_name": "Business Law Fundamentals", "keywords": ["business law", "legal regulations", "contracts"], "university": "LawBiz School"},
    {"course_name": "Data Visualization with Tableau", "keywords": ["data visualization", "Tableau", "data dashboards"], "university": "TableauViz Institute"},
    {"course_name": "Digital Content Creation", "keywords": ["digital content", "content creation", "multimedia production"], "university": "DigitalContent School"},
    {"course_name": "Strategic Management Principles", "keywords": ["strategic management", "business strategy", "strategic planning"], "university": "StratMgmt Institute"},
    {"course_name": "Ethical Leadership and Decision Making", "keywords": ["ethical leadership", "decision making", "integrity"], "university": "EthicalLead College"},
    {"course_name": "Fundamentals of Product Design", "keywords": ["product design", "design thinking", "prototyping"], "university": "ProdDesign School"},
    {"course_name": "Digital Entrepreneurship", "keywords": ["digital entrepreneurship", "online business", "startup strategies"], "university": "DigitalEntre School"},
    {"course_name": "Marketing Automation Fundamentals", "keywords": ["marketing automation", "email automation", "lead nurturing"], "university": "AutoMkt School"},
    {"course_name": "Data Analysis with Excel", "keywords": ["data analysis", "Excel", "data visualization"], "university": "ExcelAnal Institute"},
    {"course_name": "Strategic Branding and Identity", "keywords": ["strategic branding", "brand identity", "brand positioning"], "university": "BrandStrat School"},
    {"course_name": "Social Media Strategy Development", "keywords": ["social media strategy", "content planning", "engagement tactics"], "university": "SocMediaStrat College"},
    {"course_name": "Advanced Web Development Techniques", "keywords": ["web development", "advanced JavaScript", "full-stack development"], "university": "AdvWebDev Institute"},
    {"course_name": "Project Risk Management", "keywords": ["project risk management", "risk assessment", "risk mitigation"], "university": "RiskMgmt College"},
    {"course_name": "Data Analysis with Python", "keywords": ["data analysis", "Python", "data manipulation"], "university": "PythonAnal Institute"},
    {"course_name": "Strategic Innovation Management", "keywords": ["strategic innovation", "innovation strategy", "design thinking"], "university": "InnovationMgmt College"},
    {"course_name": "Digital Marketing Analytics", "keywords": ["digital marketing analytics", "marketing metrics", "data-driven marketing"], "university": "DigitalMktAnal Institute"},
    {"course_name": "Cloud Architecture and Design", "keywords": ["cloud architecture", "cloud services", "scalability"], "university": "CloudArch Institute"},
    {"course_name": "Strategic Sales Management", "keywords": ["strategic sales", "sales planning", "sales strategies"], "university": "SalesStrat College"},
    {"course_name": "Data Science for Business Analytics", "keywords": ["data science", "business analytics", "predictive modeling"], "university": "DS4Biz Institute"},
    {"course_name": "Digital Media Planning and Buying", "keywords": ["media planning", "media buying", "digital advertising"], "university": "MediaPlan Institute"},
    {"course_name": "Blockchain Applications and Use Cases", "keywords": ["blockchain applications", "blockchain use cases", "cryptocurrency"], "university": "BlockApp Institute"},
    {"course_name": "Strategic Project Management", "keywords": ["strategic project management", "project planning", "project execution"], "university": "ProjectStrat College"},
    {"course_name": "Data Visualization with Python", "keywords": ["data visualization", "Python", "matplotlib"], "university": "PythonViz Institute"},
    {"course_name": "Strategic Human Resources Management", "keywords": ["human resources management", "talent management", "HR strategy"], "university": "HRStrat Institute"},
    {"course_name": "Web Development with Python", "keywords": ["web development", "Python", "Django"], "university": "PythonWeb College"},
    {"course_name": "Business Process Improvement", "keywords": ["business process improvement", "process optimization", "continuous improvement"], "university": "BizImprovement Institute"},
    {"course_name": "Digital Product Management", "keywords": ["product management", "digital products", "product strategy"], "university": "ProdMgmt School"},
    {"course_name": "IT Service Management Essentials", "keywords": ["IT service management", "ITIL", "service desk"], "university": "ITService College"},
    {"course_name": "Advanced Networking Concepts", "keywords": ["networking", "advanced routing", "network protocols"], "university": "NetAdv School"},
    {"course_name": "Business Law Fundamentals", "keywords": ["business law", "legal regulations", "contracts"], "university": "LawBiz School"},
    {"course_name": "Data Visualization with Tableau", "keywords": ["data visualization", "Tableau", "data dashboards"], "university": "TableauViz Institute"},
    {"course_name": "Digital Content Creation", "keywords": ["digital content", "content creation", "multimedia production"], "university": "DigitalContent School"},
    {"course_name": "Strategic Management Principles", "keywords": ["strategic management", "business strategy", "strategic planning"], "university": "StratMgmt Institute"},
    {"course_name": "Ethical Leadership and Decision Making", "keywords": ["ethical leadership", "decision making", "integrity"], "university": "EthicalLead College"},
    {"course_name": "Fundamentals of Product Design", "keywords": ["product design", "design thinking", "prototyping"], "university": "ProdDesign School"},
    {"course_name": "Digital Entrepreneurship", "keywords": ["digital entrepreneurship", "online business", "startup strategies"], "university": "DigitalEntre School"},
    {"course_name": "Marketing Automation Fundamentals", "keywords": ["marketing automation", "email automation", "lead nurturing"], "university": "AutoMkt School"},
    {"course_name": "Data Analysis with Excel", "keywords": ["data analysis", "Excel", "data visualization"], "university": "ExcelAnal Institute"},
    {"course_name": "Strategic Branding and Identity", "keywords": ["strategic branding", "brand identity", "brand positioning"], "university": "BrandStrat School"},
    {"course_name": "Social Media Strategy Development", "keywords": ["social media strategy", "content planning", "engagement tactics"], "university": "SocMediaStrat College"},
    {"course_name": "Advanced Web Development Techniques", "keywords": ["web development", "advanced JavaScript", "full-stack development"], "university": "AdvWebDev Institute"},
    {"course_name": "Project Risk Management", "keywords": ["project risk management", "risk assessment", "risk mitigation"], "university": "RiskMgmt College"},
    {"course_name": "Data Analysis with Python", "keywords": ["data analysis", "Python", "data manipulation"], "university": "PythonAnal Institute"},
    {"course_name": "Strategic Innovation Management", "keywords": ["strategic innovation", "innovation strategy", "design thinking"], "university": "InnovationMgmt College"},
    {"course_name": "Digital Marketing Analytics", "keywords": ["digital marketing analytics", "marketing metrics", "data-driven marketing"], "university": "DigitalMktAnal Institute"},
    {"course_name": "Cloud Architecture and Design", "keywords": ["cloud architecture", "cloud services", "scalability"], "university": "CloudArch Institute"},
    {"course_name": "Strategic Sales Management", "keywords": ["strategic sales", "sales planning", "sales strategies"], "university": "SalesStrat College"},
    {"course_name": "Data Science for Business Analytics", "keywords": ["data science", "business analytics", "predictive modeling"], "university": "DS4Biz Institute"},
    {"course_name": "Digital Media Planning and Buying", "keywords": ["media planning", "media buying", "digital advertising"], "university": "MediaPlan Institute"},
    {"course_name": "Blockchain Applications and Use Cases", "keywords": ["blockchain applications", "blockchain use cases", "cryptocurrency"], "university": "BlockApp Institute"},
    {"course_name": "Strategic Project Management", "keywords": ["strategic project management", "project planning", "project execution"], "university": "ProjectStrat College"},
    {"course_name": "Data Visualization with Python", "keywords": ["data visualization", "Python", "matplotlib"], "university": "PythonViz Institute"},
    {"course_name": "Strategic Human Resources Management", "keywords": ["human resources management", "talent management", "HR strategy"], "university": "HRStrat Institute"}
]

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
                suggested_courses.append((course['course_name'], course['university'], match_count))
                if match_count > max_matches:
                    max_matches = match_count
            else:
                suggested_courses.sort(key=lambda x: x[2], reverse=True)
                if match_count > suggested_courses[6][2]:
                    suggested_courses.pop()
                    suggested_courses.append((course['course_name'], course['university'], match_count))
    suggested_courses.sort(key=lambda x: x[2], reverse=True)
    return [(course[0], course[1]) for course in suggested_courses]

def main():
    st.markdown(
        """
        <style>
            .main {
                background-image: linear-gradient(to bottom, #7fbfff, #55aaff);
                color: white;
                padding: 20px;
                border-radius: 10px;
            }
            h1 {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 30px;
            }
            p {
                font-size: 18px;
                margin-bottom: 10px;
            }
            .course {
                font-size: 20px;
                margin-bottom: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.image("pic.jpg", width=100)
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
            for course, university in suggested_courses:
                st.write(f"- {course} at {university}")
        else:
            st.write("No courses found based on your resume.")

if __name__ == "__main__":
    main()
