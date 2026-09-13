import streamlit as st
import pandas as pd

from agent import discover_companies


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="TVB Lead Discovery Agent",
    page_icon="🔎",
    layout="wide",
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #bbbbbb;
        margin-bottom: 25px;
    }

    .metric-box {
        padding: 20px;
        border-radius: 12px;
        background: #171923;
        border: 1px solid #30323d;
        text-align: center;
    }

    .metric-number {
        font-size: 36px;
        font-weight: 800;
    }

    .metric-label {
        font-size: 15px;
        color: #aaaaaa;
    }

    .demo-note {
        padding: 14px;
        border-radius: 8px;
        background: #19324a;
        color: #dceeff;
        margin-bottom: 20px;
    }

    .success-note {
        padding: 14px;
        border-radius: 8px;
        background: #123d25;
        color: #d9ffe5;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("⚙️ Search Settings")

    number_to_search = st.slider(
        "Number of companies to search",
        min_value=10,
        max_value=30,
        value=20,
        step=1,
    )

    st.divider()

    st.subheader("TVB Qualification Criteria")

    st.markdown("**Funding / Revenue:** `$1M–$5M`")
    st.markdown("**Business:** Technology-related platform")
    st.markdown("**US Presence:** Minimal or none")
    st.markdown("**Contact:** CEO / Co-founder")
    st.markdown("**Email:** Publicly available business email")


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🔎 TVB Lead Discovery Agent</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Automatically discover and qualify technology companies "
    "matching The Venture Build's target profile."
    "</div>",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# DEMO INFORMATION
# ---------------------------------------------------------

st.markdown(
    """
    <div class="demo-note">
    🆓 <b>Free Demo Version — No OpenAI API Key Required</b><br><br>
    The application demonstrates automated company discovery and
    transparent qualification rules using a synthetic demo dataset.
    No real contact information is invented or claimed.
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# FIND COMPANIES BUTTON
# ---------------------------------------------------------

if st.button(
    "🔎 Find Companies",
    type="primary",
    use_container_width=True,
):

    with st.spinner("Discovering and qualifying companies..."):

        companies = discover_companies(number_to_search)

    st.session_state["companies"] = companies


# ---------------------------------------------------------
# DISPLAY RESULTS
# ---------------------------------------------------------

if "companies" in st.session_state:

    companies = st.session_state["companies"]

    df = pd.DataFrame(companies)

    qualified_df = df[df["qualified"] == True].copy()

    founder_count = (
        df["founder_name"]
        .fillna("")
        .astype(str)
        .str.strip()
        .ne("")
        .sum()
    )

    email_count = (
        df["email"]
        .fillna("")
        .astype(str)
        .str.contains("@", regex=False)
        .sum()
    )


    # -----------------------------------------------------
    # COMPLETION MESSAGE
    # -----------------------------------------------------

    st.markdown(
        f"""
        <div class="success-note">
        ✅ <b>Completed.</b> Found {len(df)} company records.
        </div>
        """,
        unsafe_allow_html=True,
    )


    # -----------------------------------------------------
    # METRICS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{len(df)}</div>
                <div class="metric-label">Companies Found</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{len(qualified_df)}</div>
                <div class="metric-label">Qualified Leads</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{founder_count}</div>
                <div class="metric-label">Founder / CEO Found</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-number">{email_count}</div>
                <div class="metric-label">Public Emails</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()


    # -----------------------------------------------------
    # QUALIFIED LEADS
    # -----------------------------------------------------

    st.header("✅ Qualified Leads")

    if len(qualified_df) > 0:

        display_columns = [
            "company_name",
            "description",
            "industry",
            "country",
            "funding_or_revenue",
            "us_presence",
            "founder_name",
            "founder_role",
            "email",
            "qualification_reason",
        ]

        st.dataframe(
            qualified_df[display_columns],
            use_container_width=True,
            hide_index=True,
        )

    else:

        st.warning(
            "No fully qualified leads were found."
        )


    # -----------------------------------------------------
    # ALL COMPANIES
    # -----------------------------------------------------

    st.header("📋 All Discovered Companies")

    all_columns = [
        "company_name",
        "description",
        "industry",
        "country",
        "funding_or_revenue",
        "us_presence",
        "founder_name",
        "founder_role",
        "email",
        "qualified",
    ]

    st.dataframe(
        df[all_columns],
        use_container_width=True,
        hide_index=True,
    )


    # -----------------------------------------------------
    # QUALIFICATION DETAILS
    # -----------------------------------------------------

    st.header("🧠 Qualification Logic")

    st.markdown(
        """
        A company is marked **Qualified** only when all five
        conditions are satisfied:

        1. 💰 Funding / revenue is between **$1M and $5M**
        2. 💻 Business is **technology-related**
        3. 🇺🇸 US presence is **minimal or none**
        4. 👤 Founder / CEO information is available
        5. 📧 A business email field is available

        This rule-based approach makes the qualification
        process transparent and explainable.
        """
    )


    # -----------------------------------------------------
    # EXPORT CSV
    # -----------------------------------------------------

    st.header("📥 Export Results")

    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv_data,
        file_name="tvb_lead_discovery_results.csv",
        mime="text/csv",
        use_container_width=True,
    )


    # -----------------------------------------------------
    # IMPORTANT NOTE
    # -----------------------------------------------------

    st.divider()

    st.caption(
        "Demo note: The displayed companies and email addresses "
        "are synthetic records for project demonstration. "
        "For a production version, these fields should be populated "
        "only from verifiable public sources."
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "TVB Lead Discovery Agent | Automated company discovery "
    "and qualification | Free Rule-Based Demo"
)