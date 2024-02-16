from flask import Flask, render_template

app = Flask(__name__)

resume_data = {
    "name": "Adhish Maheswaran",
    "address": "3722 Dunrankin dr, Mississauga, Ontario",
    "phone": "343-961-5800",
    "email": "adhish0001@gmail.com",
    "linkedin": "linkedin.com/in/adhish-maheswaran-9a510a196/",
    "github": "https://github.com/adhish2001",
    "education": {
        "university": "University of Ottawa",
        "degree": "Bachelor of Applied Science Software Engineering (Engineering Management and Entrepreneurship)",
        "dates": "Sep 2019 – Dec 2023",
        "location": "Ottawa, Ontario"
    },
    "experience": [
        {
            "company": "Solace",
            "dates": "May 2023 – Aug 2023",
            "position": "Junior Software Developer-Cloud-Infra",
            "location": "Ottawa, Ontario",
            "highlights": [
                "Led security improvements by integrating static IAC tools such as tfsec and checkov scans across Terraform Modules",
                "Created and added Open Policy Agent (OPA) policies to Atlantis Terraform Pull Request automation, policy enforcement",
                "Implemented automated scans using scripts and Github Actions across the organization’s Terraform Codebase",
                "Worked on enhancing the security posture of infrastructure code by fixing vulnerabilities and ensuring adherence to best practices."
            ]
        },
        {
            "company": "Solace",
            "dates": "May 2022 – Aug 2022",
            "position": "Junior Software Developer-Cloud-Infra",
            "location": "Ottawa, Ontario",
            "highlights": [
                "Played a role in assisting the migration of the AWS cloud stack to Terraform Cloud.",
                "Utilized Kubernetes for conducting upgrades of HashiCorp Vault, a tool for managing secrets and protecting sensitive data.",
                "Worked with HashiCorp Configuration Language (HCL), the syntax used in Terraform for defining infrastructure configurations.",
                "Developed and executed scripts using Vault APIs and Python to conduct Infrastructure Reliability Testing."
            ]
        },
        {
            "company": "Shared Services Canada",
            "dates": "Sep 2021 – Dec 2021",
            "position": "Junior Software Dev",
            "location": "Ottawa, Ontario",
            "highlights": [
                "Completed DevOps tool and methodology training as part of a professional development program.",
                "Utilized Ansible in order to create playbooks for the configuration of remote servers.",
                "Orchestrated and Automated the deployment of remote servers using vRealize Automation."
            ]
        },
        {
            "company": "Software For Love",
            "dates": "Apr 2021 – Dec 2021",
            "position": "Front-End Developer",
            "location": "Ottawa, Ontario",
            "highlights": [
                "Used Gatsby, a React-based framework, to create websites with improved loading times and good performance.",
                "Used Figma, a collaborative interface design tool, to create design mock-ups for websites."
            ]
        },
        {
            "company": "Canadian Food Inspection Agency",
            "dates": "Jan 2021 – Apr 2021",
            "position": "Junior Software Dev",
            "location": "Ottawa, Ontario",
            "highlights": [
                "Setup, configurations, and any custom scripts or extensions used for Azure Pipelines were documented.",
                "Created Pipelines that are configured to automate testing, guaranteeing dependable and effective software delivery."
            ]
        }
    ],
    "projects": [
        {
            "name": "Fitshare, Fitness Application",
            "technologies": "MERN stack",
            "description": "Created a web application using MERN stack. Completed front-end with typescript, tailwind, made pages responsive and seamless. Created Selenium code to do reliability testing on front-end."
        },
        # Add other project entries here
    ],
    "technical_skills": {
        "languages": "Python, Java, JavaScript/Typescript, Terraform, YAML",
        "developer_tools": "VS Code, Google Cloud Platform, Hashicorp Cloud Services, AWS cloud",
        "technologies": "Gatsby, React.js, GitHub, Jira"
    },
    "certificates": [
        "HashiCorp Certified: Terraform Associate (003) Understanding basic concepts, skills, and use-cases of Terraform",
        "Machine Learning Skills Challenge August 2023 Microsoft Azure - Applying AI models to pipelines",
        "Cloud Practitioner Essentials October 2021 AWS learning - foundational knowledge of cloud services",
        "Basic Reliability Screening Security Clearance"
    ]
    # Add other sections like projects, technical_skills, certificates, etc.
}

@app.route('/')
def index():
    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
