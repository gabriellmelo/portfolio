# personal info (for main page) --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
info = {'brief':
              """    
                Aspiring Data Engineer with a solid foundation in software development, data analysis, and
                systems integration. Experienced in developing scalable applications and managing
                data-driven projects across financial and academic sectors. Proficient in modern
                programming languages, frameworks, and data tools, including Python, SQL, and AWS, with
                hands-on experience in building dashboards, analyzing large datasets, and implementing
                APIs. Recent projects focused on applying data visualization and AI for actionable insights.
                Passionate about leveraging data engineering to optimize processes, enhance
                decision-making, and drive innovation.
                
                *Let’s connect if you’re looking for a dedicated professional to transform data into actionable
                insights and robust solutions.*
              """,
        'name':'Gabriel Melo', 
        'study':'University of São Paulo (USP)',
        'formacao': 'Universidade de São Paulo (USP)',
        'location':'São Carlos/SP, Brazil',
        'localizacao':'São Carlos/SP, Brasil',
        'interest':'Data Engineer, Data Science',
        'interesses': 'Engenharia de Dados, Ciência de Dados',
        'skills': {
          'data': ["PostgreSQL", "Google BigQuery", "SQL", "Python (Pandas, NumPy, Matplotlib, Seaborn, Streamlit)", "Power BI"],
          'frontend': ["HTML5", "CSS3", "SCSS", "Tailwind CSS", "JavaScript", "TypeScript", "Angular", "React Native", "Ionic"],
          'backend': ["Python", "Docker", "JavaScript", "TypeScript", "Node.js", "APIs"],
          'devops': ["Docker", "GitLab (CI/CD pipelines)", "Git", "GitLab"],
          'cloud': ["AWS (QuickSight, Athena)"],
          'development_tools': ["Jupyter Notebooks", "Google Colab", "Visual Studio Code", "Android Studio", "IntelliJ IDEA"],
          'operating_systems': ["Ubuntu", "MacOS", "Windows"]
        }
      }

# Experience --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#[[header, subheader, date, location, content, link, link_url], [...], etc.]

Experience = [
              [":green[Universo Prematuro] | Social Impact Organization", "Software Engineer Volunteer", 
              "Sep 2024 – present", "Franca/SP, Brazil", 
              """
              - Developed and maintained features in the mobile application, optimizing scalability and efficiency.
              - Integrated APIs and optimized data management in the back-end.
              - Used Docker for development environments and managed version control.
              - Implemented responsive designs to ensure compatibility across devices.
              - Created dashboards to monitor service performance, enhancing analysis and decision-making.
              - Technologies: Angular, TypeScript, NestJS, PostgreSQL, Docker, GitLab, Tailwind CSS, Power BI
              """, 
              "Company website", "https://www.instagram.com/universo_prematuro?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="],

              [":blue[Unifran Jr] | Junior Enterprise", "Data Analyst", 
              "Feb 2024 – Nov 2024", "Franca/SP, Brazil", 
              """
              - Conducted market analysis by gathering relevant and up-to-date data from official sources to identify patterns and trends.
              - Filtered and queried large datasets to optimize data processing and extraction of valuable insights.
              - Developed graphs and data visualizations to facilitate understanding, using Python for data analysis and visualization.
              - Collaborated with a multidisciplinary team of students to design data-driven business strategies.
              - Technologies: Google BigQuery, SQL, Python, Matplotlib, Pandas, NumPy
              """,
              "Company website", "https://www.instagram.com/unifranjr?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="],

              [":orange[Itaú Unibanco] | Bank", "Frontend Junior Developer", 
              "Aug 2022 – Sep 2024", "Remote", 
              """
              - Contributed to the maintenance and implementation of new features for Banco Itaú’s SuperApp, specifically for the “Cheque Especial/Limite da Conta” product, a service offering a special credit line for customers to cover withdrawals exceeding their available balance.
              - Utilized Angular and TypeScript for front-end development, ensuring high performance and quality.
              - Regularly filled out Change Management Documentation for production deployments, detailing the features to be implemented.
              - Monitored production pipelines on AWS, tracking deployment processes to ensure successful deliveries or rollback when necessary, minimizing impact on users.
              - Technologies: JavaScript, TypeScript, Angular, AWS
              """,
              "Company website", "https://www.itau.com.br"
              ],
              [
                  ":orange[Itaú Unibanco] | Bank", "Subject Matter Expert", 
                  "Jan 2022 – Aug 2022", "Remote", 
                  """
                  - Oversaw technology deliveries in the insurance sector at the community level, managing the end-to-end delivery of solutions used by thousands of clients.
                  - Regularly presented progress reports and updates on key project deliveries to senior management and executives, ensuring visibility and strategic alignment.
                  - Facilitated communication between stakeholders, coordinating project timelines and negotiating deadlines to ensure timely deliveries.
                  - Technologies: Excel, PowerPoint
                  """,
                  "Company website", "https://www.itau.com.br"
              ],
              [
                  ":orange[Itaú Unibanco] | Bank", "Scrum Master", 
                  "Oct 2021 – Dec 2021", "Remote", 
                  """
                  - Led agile ceremonies (planning, retrospectives, and dailies), promoting team maturity and adoption of best agile practices.
                  - Managed risks and impediments, monitoring key performance indicators (KPIs) to ensure continuous improvement.
                  - Fostered a collaborative environment, helping the team achieve success in delivering projects within an agile framework.
                  - Technologies: Jira, PowerPoint
                  """,
                  "Company website", "https://www.itau.com.br"
              ],

              ["Brandeis :orange[Quant Club]", "Software Engineer", 
                "Jan 2023 – Sep 2023", "Waltham, MA", 
                """
                - Contribute to research, gather, and analyze information of different companies where we show users companies’ volatility indices using Python.
                - Designed and developed a website that allows users to see data regarding companies’ volatility indices utilizing **JavaScript, React, and Node.js** (setting up the website’s skeleton, capable of automatically giving users the most up-to-date information).
                """,
              "Club website", "https://brandeisquantclub.org"],

              [":orange[Brandeis University] | Anthropology Department", "Research Assistant",
                "Sep 2022 – Aug 2023", "Waltham, MA", 
                """
                - Collaborated with Anthropology professor Elizabeth Ferry on researching asset tokenization and cryptocurrencies as cultural phenomena.
                - Interviewed 17 people who worked in Finance and IT industry during the summer; asking about their opinion on Gold Tokenization, Bitcoin, Blockchain, and Central Bank digital Currency in China. These finding support and enrich Professor Ferry’s ongoing book writing about Gold in mining and finance.
                - Weekly report based on searching for and reading news, social media reports, and journalistic and academic analyses.
                """,
                "Department website", "https://www.brandeis.edu/anthropology/undergraduate/research-and-funding/student-bios.html"],

              [":violet[Branda] | Brandeis Campus App", "Software Engineer", 
              "Jan 2023 – present", "Waltham, MA", 
              """
              - Collaborated in a **Agile** software development cycle, main responsible for improving the mobile UI/UX.
              - Implemented a interactive calendar daily used by 1.6K student to keep track of school events, using **REST APIs** with **React Native** as the front-end. Utilized **Redis** to cache hotspot data, reducing the workload on main database.
              - Managed database migration from Heroku to **Firebase** to meet user growth, implemented API touchpoints within the CI/CD pipeline for migration testing.
              """,
              "App Store link", "https://apps.apple.com/us/app/branda/id1437022581"]
              ]      

# Portfolio --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # {'project1':[HEADER, CONTENT]
    #  'project2':[HEADER, CONTENT]
    #  ...}

Portfolio = { 1:[':blue[Deis]Evaluation - Course Evaluation Website',
              """
              Launched a course evaluation web app for Brandeis students to review and share courses, exceeding 200+ active users.
              Designed the whole UI with Figma and Implemented front end with Javascript, HTML/CSS in a MERN Stack.
              """],
              2:['Data Visualization in :orange[D3.js]',
                  """
                Created a data visualization web app for Massachusetts police expenditure data using D3.js.
                """],
              3:[':blue[LLM] Desktop ChatApp',
                """
                - Designed and developed a cross-platform **desktop LLM Chat app**, enabling chat over user-upload dataset; providing a more accurate response to domain-specific inquiries than ChatGPT.
                - Utilized Embedding and Searching from **OpenAI API** to optimize Chat app’s response. Split the user-upload file into small chunks; used OpenAI Embedding model to vectorize each chunk and save them into Qdrant database. Transform user query to vector using OpenAI, and then inquire the top match text chunk from Qdrant database using topk value.
                """],
              4:[':orange[Anthropology] Research Project - A Timeless Building',
                """
                - An **qualitative anthropological research** on the preservation and adaption of historical sites; as final project, received the highest score in class.
                - My fieldwork includes interviewing educators, examing archive, on-site obervation. Through my fieldwork at King’s Chapel, I argued for a humane approach to preserving historic sites, that seeks a balance between **maintaining the historical significance and the sites’ adaptations to societal changes**.
                """],
              5:[':green[RAG] playground',  
                """
                - Developed a **RAG** chatbot that support difference choices over Embedding model, chunking strategy, top k retreival, LLM model, prompt engineering, and meta-data retreival search.
                - Implemented the file uploading workflow; Utilized **Langchain splitter** module and Python script to clean and chunk the uploaded file and use Huggingface sentence transformers and **Pinecone** to vectorize and store data.
                - Used SpaCy NER model to retreive meta data from prompt and ran a hybrid search using meta-data and vector.
                """]
            }
              
# Contacts --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
phone = "(16) 9 8105-0390"
email = "contato@gabrielmelo.com"
linkedin_link = "https://www.linkedin.com/in/gabriellmelo/"
github_link = "https://github.com/gabriellmelo"