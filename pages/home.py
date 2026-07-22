import streamlit as st

# Custom CSS to match the design in the screenshots
st.markdown(
    """
    <style>
        /* Hero Card Styling */
        .home-hero {
            background: linear-gradient(90deg, #14234b 0%, #2962ff 100%);
            padding: 2.5rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .home-hero .eyebrow {
            font-size: 0.9rem;
            color: #cbd5e1;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 0.5rem;
            background-color: rgba(255, 255, 255, 0.1);
            display: inline-block;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }
        .home-hero h1 {
            color: white !important;
            font-size: 2.8rem !important;
            font-weight: 800;
            margin: 0.5rem 0;
            padding: 0;
        }
        .home-hero h2 {
            color: white !important;
            font-size: 1.4rem !important;
            font-weight: 600;
            margin: 0 0 1rem 0;
            padding: 0;
        }
        .home-hero p {
            color: #f1f5f9 !important;
            font-size: 1.05rem;
            line-height: 1.5;
            margin: 0;
        }

        /* Standard White Cards */
        .page-card {
            background-color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        }
        .page-card h2 {
            color: #0f172a !important; /* Dark text to fix visibility issue */
            font-size: 1.5rem !important;
            font-weight: 700;
            margin-top: 0;
            padding-top: 0;
        }
        .page-card p {
            color: #475569 !important;
            line-height: 1.6;
            margin-bottom: 0;
        }

        /* Feature Cards (3 columns) */
        .feature-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            height: 100%;
        }
        .feature-card h3 {
            color: #0f172a !important;
            font-size: 1.2rem !important;
            font-weight: 700;
            margin-top: 0;
            padding-top: 0;
        }
        .feature-card p {
            color: #475569 !important;
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 0;
        }

        /* Tech Stack Pills */
        .stack-pill-container {
            margin-top: 1rem;
        }
        .stack-pill {
            display: inline-block;
            background-color: #e0f2fe; /* Light blue background */
            color: #0284c7; /* Dark blue text */
            padding: 0.4rem 1rem;
            border-radius: 9999px; /* Pill shape */
            font-size: 0.9rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
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