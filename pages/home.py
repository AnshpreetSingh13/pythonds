import streamlit as st

# Custom CSS to match the design in the screenshots
st.markdown(
    """
    <style>
        .home-hero {
            background: linear-gradient(135deg, #071426 0%, #11233b 45%, #1d4ed8 100%);
            padding: 2.3rem;
            border-radius: 24px;
            color: white;
            margin-bottom: 1.4rem;
            box-shadow: 0 20px 50px rgba(2, 6, 23, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .home-hero .eyebrow {
            font-size: 0.8rem;
            color: #7dd3fc;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            margin-bottom: 0.55rem;
            background: rgba(125, 211, 252, 0.14);
            display: inline-block;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            border: 1px solid rgba(125, 211, 252, 0.18);
        }
        .home-hero h1 {
            color: white !important;
            font-size: 2.6rem !important;
            font-weight: 800;
            margin: 0.35rem 0;
            padding: 0;
        }
        .home-hero h2 {
            color: white !important;
            font-size: 1.2rem !important;
            font-weight: 600;
            margin: 0 0 0.9rem 0;
            padding: 0;
        }
        .home-hero p {
            color: #e2e8f0 !important;
            font-size: 1rem;
            line-height: 1.6;
            margin: 0;
        }

        .page-card {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.9));
            color: #f8fafc;
            padding: 1.4rem 1.6rem;
            border-radius: 22px;
            margin-bottom: 1.2rem;
            box-shadow: 0 16px 40px rgba(2, 6, 23, 0.24);
            border: 1px solid rgba(148, 163, 184, 0.18);
        }
        .page-card h2 {
            color: #f8fafc !important;
            font-size: 1.25rem !important;
            font-weight: 700;
            margin-top: 0;
            padding-top: 0;
        }
        .page-card p {
            color: #cbd5e1 !important;
            line-height: 1.6;
            margin-bottom: 0;
        }

        .feature-card {
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.9));
            padding: 1.4rem;
            border-radius: 20px;
            box-shadow: 0 16px 40px rgba(2, 6, 23, 0.24);
            border: 1px solid rgba(148, 163, 184, 0.18);
            height: 100%;
        }
        .feature-card h3 {
            color: #f8fafc !important;
            font-size: 1.08rem !important;
            font-weight: 700;
            margin-top: 0;
            padding-top: 0;
        }
        .feature-card p {
            color: #cbd5e1 !important;
            font-size: 0.94rem;
            line-height: 1.55;
            margin-bottom: 0;
        }

        .stack-pill-container {
            margin-top: 1rem;
        }
        .stack-pill {
            display: inline-block;
            background: rgba(96, 165, 250, 0.14);
            color: #bfdbfe;
            padding: 0.42rem 0.85rem;
            border-radius: 999px;
            font-size: 0.86rem;
            font-weight: 700;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            border: 1px solid rgba(96, 165, 250, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <div class="home-hero">
        <div class="eyebrow">Global Workforce Intelligence</div>
        <h1>TECHLAYOFFS</h1>
        <h2>Global Tech Layoff Analytics Dashboard</h2>
        <p>
            TECHLAYOFFS is a premium analytics platform built to turn workforce, business, and market signals into
            clear executive-ready insights. The project was created to help HR teams, leaders, and analysts understand
            layoffs, hiring pressure, financial movement, remote work trends, and AI-driven transformation in one place.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Intro Card
st.markdown(
    """
    <div class="page-card">
        <h2>Why this project exists</h2>
        <p>
            In a fast-changing tech environment, organizations need quick visibility into how workforce decisions affect
            business health. TECHLAYOFFS brings together key signals from layoffs, hiring, budgets, employee sentiment,
            company size, and market conditions so stakeholders can make more informed decisions.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 3-Column Layout
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>For HR Teams</h3>
            <p>Monitor workforce stability, hiring momentum, talent risk, and employee sentiment through interactive dashboards.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>For Business Leaders</h3>
            <p>Track financial direction, revenue growth, salary changes, and market conditions with executive-level clarity.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>For Analysts</h3>
            <p>Explore detailed charts and metrics that connect operations, people strategy, and business performance.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True) # Adds a little spacing before the next card

# Included features card
st.markdown(
    """
    <div class="page-card">
        <h2>What the dashboard includes</h2>
        <p>
            Executive summaries, layoff and hiring analytics, AI impact insights, business performance metrics,
            and premium visual storytelling designed for better decision-making.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Tech Stack Card
st.markdown(
    """
    <div class="page-card">
        <h2>Technology Stack</h2>
        <div class="stack-pill-container">
            <span class="stack-pill">Python</span>
            <span class="stack-pill">Pandas</span>
            <span class="stack-pill">NumPy</span>
            <span class="stack-pill">Plotly</span>
            <span class="stack-pill">Streamlit</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)