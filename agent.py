"""
TVB Lead Discovery Agent
Free demo version - no OpenAI API required.

NOTE:
The records below are SYNTHETIC DEMO DATA.
They are intentionally not presented as real companies or real contact details.
"""

from typing import List, Dict


DEMO_COMPANIES = [
    {
        "company_name": "NovaTech Platforms",
        "description": "Technology-focused SaaS platform for business automation.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$2 million",
        "funding_value": 2.0,
        "us_presence": "Minimal / none",
        "founder_name": "Aarav Sharma",
        "founder_role": "Founder / CEO",
        "email": "hello@novatech.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "CloudBridge Technologies",
        "description": "Cloud-based technology platform providing business software solutions.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$3 million",
        "funding_value": 3.0,
        "us_presence": "Minimal / none",
        "founder_name": "Riya Patel",
        "founder_role": "Co-founder",
        "email": "contact@cloudbridge.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "DataFlow Labs",
        "description": "Data and analytics platform helping companies automate reporting.",
        "industry": "Technology",
        "country": "Singapore",
        "funding_or_revenue": "$4 million",
        "funding_value": 4.0,
        "us_presence": "Minimal / none",
        "founder_name": "Daniel Tan",
        "founder_role": "Founder / CEO",
        "email": "hello@dataflow.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "PixelGrid Systems",
        "description": "Digital technology platform for workflow and productivity management.",
        "industry": "Technology",
        "country": "United Kingdom",
        "funding_or_revenue": "$1.5 million",
        "funding_value": 1.5,
        "us_presence": "Minimal / none",
        "founder_name": "Oliver Smith",
        "founder_role": "Co-founder",
        "email": "team@pixelgrid.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "TechOrbit Solutions",
        "description": "B2B software platform focused on digital business solutions.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$5 million",
        "funding_value": 5.0,
        "us_presence": "Minimal / none",
        "founder_name": "Neha Mehta",
        "founder_role": "Founder / CEO",
        "email": "info@techorbit.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "BrightStack",
        "description": "Technology platform offering cloud tools for growing businesses.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$2.5 million",
        "funding_value": 2.5,
        "us_presence": "Minimal / none",
        "founder_name": "Kabir Shah",
        "founder_role": "Founder",
        "email": "hello@brightstack.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "CodeNest Technologies",
        "description": "Developer-focused platform providing software development tools.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$1.8 million",
        "funding_value": 1.8,
        "us_presence": "Minimal / none",
        "founder_name": "Ananya Joshi",
        "founder_role": "Co-founder",
        "email": "contact@codenest.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "FinCloud Platform",
        "description": "Technology platform providing cloud-based financial workflow tools.",
        "industry": "Technology",
        "country": "Singapore",
        "funding_or_revenue": "$3.5 million",
        "funding_value": 3.5,
        "us_presence": "Minimal / none",
        "founder_name": "Marcus Lim",
        "founder_role": "Founder / CEO",
        "email": "hello@fincloud.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "AutomateX",
        "description": "AI-enabled automation platform for small and medium businesses.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$4.2 million",
        "funding_value": 4.2,
        "us_presence": "Minimal / none",
        "founder_name": "Vikram Rao",
        "founder_role": "Founder / CEO",
        "email": "team@automatex.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "NextWave Digital",
        "description": "Digital transformation platform for modern businesses.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$2.2 million",
        "funding_value": 2.2,
        "us_presence": "Minimal / none",
        "founder_name": "Ishita Verma",
        "founder_role": "Co-founder",
        "email": "info@nextwave.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "SecureSphere",
        "description": "Cybersecurity technology platform for growing organizations.",
        "industry": "Technology",
        "country": "United Kingdom",
        "funding_or_revenue": "$4.8 million",
        "funding_value": 4.8,
        "us_presence": "Minimal / none",
        "founder_name": "James Wilson",
        "founder_role": "Founder / CEO",
        "email": "hello@securesphere.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "MarketPilot",
        "description": "Technology platform helping businesses manage digital marketing workflows.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$1.2 million",
        "funding_value": 1.2,
        "us_presence": "Minimal / none",
        "founder_name": "Sahil Kapoor",
        "founder_role": "Founder",
        "email": "contact@marketpilot.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "DevSphere",
        "description": "Cloud technology platform for software teams and developers.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$3.8 million",
        "funding_value": 3.8,
        "us_presence": "Minimal / none",
        "founder_name": "Meera Nair",
        "founder_role": "Co-founder",
        "email": "hello@devsphere.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "SmartOps Technologies",
        "description": "Business operations platform using automation and analytics.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$2.7 million",
        "funding_value": 2.7,
        "us_presence": "Minimal / none",
        "founder_name": "Rahul Desai",
        "founder_role": "Founder / CEO",
        "email": "team@smartops.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "CloudMint",
        "description": "Cloud technology platform designed for business process automation.",
        "industry": "Technology",
        "country": "Singapore",
        "funding_or_revenue": "$4.5 million",
        "funding_value": 4.5,
        "us_presence": "Minimal / none",
        "founder_name": "Kevin Wong",
        "founder_role": "Founder / CEO",
        "email": "info@cloudmint.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "AppForge",
        "description": "Low-code technology platform for creating business applications.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$1.7 million",
        "funding_value": 1.7,
        "us_presence": "Minimal / none",
        "founder_name": "Priya Shah",
        "founder_role": "Co-founder",
        "email": "hello@appforge.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "AIWorks Platform",
        "description": "AI-powered business technology platform for workflow automation.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$3.2 million",
        "funding_value": 3.2,
        "us_presence": "Minimal / none",
        "founder_name": "Arjun Malhotra",
        "founder_role": "Founder / CEO",
        "email": "contact@aiworks.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "BizTech Cloud",
        "description": "B2B technology platform supporting digital business operations.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$2.9 million",
        "funding_value": 2.9,
        "us_presence": "Minimal / none",
        "founder_name": "Kavya Patel",
        "founder_role": "Founder",
        "email": "hello@biztech.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "DataPilot",
        "description": "Analytics and data management platform for technology businesses.",
        "industry": "Technology",
        "country": "United Kingdom",
        "funding_or_revenue": "$4 million",
        "funding_value": 4.0,
        "us_presence": "Minimal / none",
        "founder_name": "Thomas Brown",
        "founder_role": "Co-founder",
        "email": "team@datapilot.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
    {
        "company_name": "GrowthGrid",
        "description": "Technology platform providing tools for business growth and automation.",
        "industry": "Technology",
        "country": "India",
        "funding_or_revenue": "$1.9 million",
        "funding_value": 1.9,
        "us_presence": "Minimal / none",
        "founder_name": "Aditya Singh",
        "founder_role": "Founder / CEO",
        "email": "hello@growthgrid.example",
        "email_source": "Company demo contact page",
        "company_source": "Public web demo dataset",
    },
]


def qualify_company(company: Dict) -> Dict:
    """
    Apply TVB qualification rules.

    Rules:
    1. Funding/revenue must be between $1M and $5M.
    2. Business must be technology related.
    3. US presence must be minimal or none.
    4. Founder/CEO must be available.
    5. Public business email must be available.
    """

    funding_ok = 1.0 <= company["funding_value"] <= 5.0

    industry_text = company["industry"].lower()
    business_ok = any(
        word in industry_text
        for word in ["technology", "software", "saas", "platform", "ai", "cloud"]
    )

    us_ok = company["us_presence"].lower() in [
        "minimal / none",
        "none",
        "minimal",
    ]

    founder_ok = (
        bool(company.get("founder_name"))
        and company.get("founder_role", "").lower()
        in ["founder", "founder / ceo", "ceo", "co-founder"]
    )

    email_ok = bool(company.get("email")) and "@" in company["email"]

    qualified = all(
        [
            funding_ok,
            business_ok,
            us_ok,
            founder_ok,
            email_ok,
        ]
    )

    reasons = []

    if funding_ok:
        reasons.append("Funding/revenue is within $1M–$5M")
    else:
        reasons.append("Funding/revenue is outside target range")

    if business_ok:
        reasons.append("Technology-related business")
    else:
        reasons.append("Not technology-related")

    if us_ok:
        reasons.append("Minimal or no US presence")
    else:
        reasons.append("Significant US presence")

    if founder_ok:
        reasons.append("Founder/CEO contact identified")
    else:
        reasons.append("Founder/CEO not identified")

    if email_ok:
        reasons.append("Public business email available")
    else:
        reasons.append("Public email not available")

    result = dict(company)

    result["qualified"] = qualified
    result["qualification_reason"] = "; ".join(reasons)

    return result


def discover_companies(number_to_search: int = 20) -> List[Dict]:
    """
    Return demo company records.

    Supports 10–30 from the Streamlit interface.
    """

    number_to_search = int(number_to_search)

    if number_to_search < 10:
        number_to_search = 10

    if number_to_search > 30:
        number_to_search = 30

    # Repeat the dataset if the user selects more than 20.
    records = []

    for i in range(number_to_search):
        company = dict(DEMO_COMPANIES[i % len(DEMO_COMPANIES)])

        # Make duplicate demo records distinguishable when >20 is selected.
        if i >= len(DEMO_COMPANIES):
            company["company_name"] = (
                company["company_name"] + f" Demo {i + 1}"
            )

        records.append(qualify_company(company))

    return records