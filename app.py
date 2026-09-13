import streamlit as st
import pandas as pd
import time

from agent import run_agent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="TVB Lead Discovery Agent",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

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

    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 22px 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .metric-icon {
        font-size: 28px;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 38px;
        font-weight: 800;
        color: #38bdf8;
        line-height: 1.1;
        margin-bottom: 6px;
    }

    .metric-label {
        font-size: 13px;
        font-weight: 600;
        color: #cbd5e1;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .info-note {
        padding: 18px;
        border-radius: 10px;
        background: #19324a;
        color: #dceeff;
        margin-bottom: 20px;
    }

    .success-note {
        padding: 18px;
        border-radius: 10px;
        background: #123d28;
        color: #d9ffe8;
        margin-bottom: 20px;
    }

    .warning-note {
        padding: 18px;
        border-radius: 10px;
        background: #493817;
        color: #fff1c7;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "agent_result" not in st.session_state:
    st.session_state["agent_result"] = run_agent(target=20)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Agent Settings")

    target_leads = st.slider(
        "Target verified leads",
        min_value=1,
        max_value=30,
        value=20,
        step=1,
    )

    max_candidates = st.slider(
        "Maximum candidates to investigate",
        min_value=50,
        max_value=300,
        value=150,
        step=25,
    )

    st.divider()

    st.subheader("🎯 TVB Qualification Criteria")

    st.markdown(
        "💰 **Funding / Revenue:** $1M – $5M"
    )

    st.markdown(
        "💻 **Business:** Technology-related platform"
    )

    st.markdown(
        "🇺🇸 **US Presence:** Minimal or none"
    )

    st.markdown(
        "👤 **Contact:** CEO / Founder / Co-founder"
    )

    st.markdown(
        "📧 **Email:** Exact public business email"
    )

    st.markdown(
        "🌐 **Source:** Public web evidence"
    )

    st.markdown(
        "✅ **Verification:** MX + SMTP when possible"
    )

    st.divider()

    st.subheader("🔗 TVB References")

    st.markdown(
        "• [LinkedIn](https://linkedin.com/company/90924902/)"
    )

    st.markdown(
        "• [The Venture Build](http://theventurebuild.com/)"
    )

    st.divider()

    st.caption(
        "The agent does not create guessed, "
        "synthetic or fabricated email addresses."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🔎 TVB Lead Discovery Agent'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    "Autonomous public-web discovery and qualification "
    "of technology companies matching The Venture Build's profile."
    "</div>",
    unsafe_allow_html=True,
)


# ============================================================
# INFORMATION BOX
# ============================================================

st.markdown(
    """
    <div class="info-note">

    <b>🤖 Autonomous Lead Discovery</b><br><br>

    The agent searches multiple public web sources,
    discovers potential companies, investigates their
    funding/revenue, technology profile, location,
    founder/CEO information and public business email.

    <br><br>

    <b>🔐 No Fabrication:</b>
    The application does not generate guessed email addresses.
    A lead is shown as verified only when the required evidence
    is available.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# RUN AGENT BUTTON
# ============================================================

run_button = st.button(
    "🔎 Find Verified Leads",
    type="primary",
    use_container_width=True,
)


if run_button:

    st.session_state["agent_result"] = None

    status_box = st.empty()

    progress_bar = st.progress(
        0,
        text="Starting autonomous discovery...",
    )

    try:

        status_box.info(
            "🌐 Searching public web sources..."
        )

        progress_bar.progress(
            10,
            text="Discovering companies..."
        )

        result = run_agent(
            target=target_leads,
            max_candidates=max_candidates,
        )

        progress_bar.progress(
            100,
            text="Completed."
        )

        time.sleep(0.5)

        status_box.empty()

        st.session_state[
            "agent_result"
        ] = result

        st.rerun()

    except Exception as e:

        progress_bar.empty()
        status_box.empty()

        st.error(
            f"❌ Agent error: {str(e)}"
        )

        st.exception(e)


# ============================================================
# DISPLAY RESULTS
# ============================================================

result = st.session_state.get(
    "agent_result"
)


if result is not None:

    # ========================================================
    # READ RESULT
    # ========================================================

    if isinstance(result, dict):

        leads = result.get(
            "leads",
            result.get(
                "qualified_leads",
                [],
            ),
        )

        all_candidates = result.get(
            "all_candidates",
            result.get(
                "candidates",
                [],
            ),
        )

    else:

        leads = result
        all_candidates = result


    # ========================================================
    # DATAFRAMES
    # ========================================================

    leads_df = pd.DataFrame(
        leads
    )

    candidates_df = pd.DataFrame(
        all_candidates
    )


    # ========================================================
    # EXPECTED COLUMNS
    # ========================================================

    expected_columns = [
        "company_name",
        "description",
        "industry",
        "country",
        "website",
        "funding_or_revenue",
        "us_presence",
        "founder_name",
        "founder_role",
        "email",
        "email_verified",
        "verification_method",
        "email_source",
        "qualification_reason",
        "sources",
    ]


    for column in expected_columns:

        if column not in leads_df.columns:

            leads_df[column] = ""


    for column in expected_columns:

        if column not in candidates_df.columns:

            candidates_df[column] = ""


    # ========================================================
    # METRICS
    # ========================================================

    verified_email_count = 0

    if not leads_df.empty:

        verified_email_count = (
            leads_df[
                "email_verified"
            ]
            .astype(str)
            .str.lower()
            .isin(
                [
                    "true",
                    "1",
                    "yes",
                    "pass",
                ]
            )
            .sum()
        )


    founder_count = 0

    if not leads_df.empty:

        founder_count = (
            leads_df[
                "founder_name"
            ]
            .fillna("")
            .astype(str)
            .str.strip()
            .ne("")
            .sum()
        )


    # ========================================================
    # COMPLETION MESSAGE
    # ========================================================

    if len(leads_df) >= target_leads:

        st.markdown(
            f"""
            <div class="success-note">

            <b>✅ Target Reached</b><br><br>

            {len(leads_df)} verified TVB leads
            were successfully discovered.

            </div>
            """,
            unsafe_allow_html=True,
        )

    elif len(leads_df) > 0:

        st.markdown(
            f"""
            <div class="warning-note">

            <b>⚠️ Partial Result</b><br><br>

            {len(leads_df)} verified leads were found.
            Target was {target_leads}.

            <br><br>

            No fake leads were added.

            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.warning(
            "No verified TVB leads were found."
        )

        st.info(
            "Try increasing the maximum candidates "
            "and run the agent again."
        )


    # ========================================================
    # METRIC CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4
    )


    with col1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">🔍</div>
                <div class="metric-value">{len(candidates_df)}</div>
                <div class="metric-label">Candidates Investigated</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with col2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">✅</div>
                <div class="metric-value" style="color: #4ade80;">{len(leads_df)}</div>
                <div class="metric-label">Verified TVB Leads</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with col3:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">👤</div>
                <div class="metric-value" style="color: #a78bfa;">{founder_count}</div>
                <div class="metric-label">Founder / CEO Found</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    with col4:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">📧</div>
                <div class="metric-value" style="color: #f472b6;">{verified_email_count}</div>
                <div class="metric-label">Verified Emails</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.divider()


    # ========================================================
    # VERIFIED LEADS TABLE
    # ========================================================

    if not leads_df.empty:

        st.header(
            "✅ Verified TVB Leads"
        )

        display_columns = [
            "company_name",
            "description",
            "industry",
            "country",
            "website",
            "funding_or_revenue",
            "us_presence",
            "founder_name",
            "founder_role",
            "email",
            "email_verified",
            "verification_method",
        ]


        display_leads_df = leads_df[display_columns].copy()
        display_leads_df["email"] = display_leads_df["email"].apply(
            lambda e: f"mailto:{e}" if e and not str(e).startswith("mailto:") else e
        )

        st.dataframe(
            display_leads_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "website": st.column_config.LinkColumn("Website"),
                "email": st.column_config.LinkColumn(
                    "Email",
                    display_text=r"mailto:(.*)",
                ),
            },
        )


        # ====================================================
        # LEAD DETAILS
        # ====================================================

        st.header(
            "🔍 Lead Verification Details"
        )


        for index, lead in leads_df.iterrows():

            company_name = (
                lead.get(
                    "company_name",
                    "Unknown Company",
                )
                or "Unknown Company"
            )


            with st.expander(
                f"{index + 1}. {company_name}"
            ):

                col1, col2 = st.columns(
                    2
                )


                with col1:

                    st.write(
                        "**Company:**",
                        lead.get(
                            "company_name",
                            "",
                        ),
                    )

                    website = lead.get(
                        "website",
                        "",
                    )

                    if website:
                        st.markdown(
                            f"**Website:** [{website}]({website})"
                        )
                    else:
                        st.write(
                            "**Website:** Not available"
                        )

                    st.write(
                        "**Industry:**",
                        lead.get(
                            "industry",
                            "",
                        ),
                    )

                    st.write(
                        "**Country:**",
                        lead.get(
                            "country",
                            "",
                        ),
                    )

                    st.write(
                        "**Funding / Revenue:**",
                        lead.get(
                            "funding_or_revenue",
                            "",
                        ),
                    )

                    st.write(
                        "**US Presence:**",
                        lead.get(
                            "us_presence",
                            "",
                        ),
                    )


                with col2:

                    st.write(
                        "**Founder / CEO:**",
                        lead.get(
                            "founder_name",
                            "",
                        ),
                    )

                    st.write(
                        "**Role:**",
                        lead.get(
                            "founder_role",
                            "",
                        ),
                    )

                    email = lead.get(
                        "email",
                        "",
                    )

                    if email:
                        st.markdown(
                            f"**Email:** [{email}](mailto:{email})"
                        )
                    else:
                        st.write(
                            "**Email:** Not available"
                        )

                    st.write(
                        "**Email Verified:**",
                        lead.get(
                            "email_verified",
                            "",
                        ),
                    )

                    st.write(
                        "**Verification Method:**",
                        lead.get(
                            "verification_method",
                            "",
                        ),
                    )


                st.write(
                    "**Description:**"
                )

                st.write(
                    lead.get(
                        "description",
                        "",
                    )
                )


                st.write(
                    "**Email Source:**"
                )

                email_source = lead.get(
                    "email_source",
                    "",
                )

                if email_source:

                    st.markdown(
                        f"[Open email source]({email_source})"
                    )

                else:

                    st.write(
                        "Not available"
                    )


                st.write(
                    "**Qualification Reason:**"
                )

                st.write(
                    lead.get(
                        "qualification_reason",
                        "",
                    )
                )


                st.write(
                    "**Sources:**"
                )

                sources = lead.get(
                    "sources",
                    [],
                )


                if isinstance(
                    sources,
                    list,
                ):

                    for source in sources:

                        if source:

                            st.markdown(
                                f"- [{source}]({source})"
                            )

                elif sources:

                    st.markdown(
                        f"- [{sources}]({sources})"
                    )


    # ========================================================
    # ALL CANDIDATES
    # ========================================================

    st.header(
        "📋 All Investigated Candidates"
    )


    if candidates_df.empty:

        st.info(
            "No candidates were returned by the agent."
        )

    else:

        candidate_columns = [
            "company_name",
            "description",
            "industry",
            "country",
            "website",
            "funding_or_revenue",
            "us_presence",
            "founder_name",
            "founder_role",
            "email",
            "email_verified",
            "qualification_reason",
        ]


        display_candidates_df = candidates_df[candidate_columns].copy()
        display_candidates_df["email"] = display_candidates_df["email"].apply(
            lambda e: f"mailto:{e}" if e and not str(e).startswith("mailto:") else e
        )

        st.dataframe(
            display_candidates_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "website": st.column_config.LinkColumn("Website"),
                "email": st.column_config.LinkColumn(
                    "Email",
                    display_text=r"mailto:(.*)",
                ),
            },
        )


    # ========================================================
    # QUALIFICATION LOGIC
    # ========================================================

    st.header(
        "🧠 Qualification Logic"
    )


    st.markdown(
        """
        A company is shown as a verified TVB lead only when
        the agent finds supporting public evidence for the
        following conditions:

        **1. 💰 Funding / Revenue**

        Between **$1M and $5M USD**.

        **2. 💻 Technology Business**

        The company operates a technology-related platform,
        SaaS product, software, AI platform, fintech platform,
        data platform or similar technology business.

        **3. 🇺🇸 US Presence**

        No explicit significant US headquarters or US presence
        is detected in the collected evidence.

        **4. 👤 Founder / CEO**

        A CEO, Founder or Co-founder is identified.

        **5. 📧 Exact Public Email**

        The email must be publicly discoverable and associated
        with the identified founder/CEO.

        **6. ✅ Email Verification**

        The email domain must have valid MX records.
        SMTP verification is attempted when the mail server
        permits it.

        **🚫 No fabricated data**

        The agent does not generate guessed email addresses
        or synthetic companies.
        """
    )


    # ========================================================
    # EXPORT
    # ========================================================

    if not leads_df.empty:

        st.header(
            "📥 Export Results"
        )


        export_df = leads_df.copy()


        # Convert list columns to readable text
        if "sources" in export_df.columns:

            export_df[
                "sources"
            ] = export_df[
                "sources"
            ].apply(
                lambda x: "\n".join(x)
                if isinstance(x, list)
                else str(x)
            )


        csv_data = (
            export_df
            .to_csv(
                index=False
            )
            .encode("utf-8")
        )


        st.download_button(
            label="⬇️ Download Verified Leads CSV",
            data=csv_data,
            file_name="tvb_verified_leads.csv",
            mime="text/csv",
            use_container_width=True,
        )


    # ========================================================
    # FOOTER
    # ========================================================

    st.divider()

    st.caption(
        "TVB Lead Discovery Agent | "
        "Autonomous public-web discovery | "
        "Evidence-based qualification | "
        "No fabricated leads"
    )