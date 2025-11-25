"""
ATS-NSE-Stock-Suite Dashboard
==============================

Mobile-first, responsive Streamlit dashboard for NSE stock market analysis.
Features include market overview, interactive charts, top movers, and global markets.

Author: Mandar Bahadarpurkar
"""

import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import pandas as pd
from mock_nse_data import MockNSEData
from nse_data_fetcher import NSEDataFetcher

# Page configuration - must be first Streamlit command
st.set_page_config(
    page_title="ATS-NSE Stock Suite",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/mandarab76/ATS-NSE-Stock-Suite',
        'About': "ATS-NSE Stock Market Analysis Suite - Developed by Mandar Bahadarpurkar"
    }
)

# Custom CSS for mobile-first responsive design
st.markdown("""
<style>
    /* Mobile-first responsive design */
    .main > div {
        padding-top: 1rem;
    }
    
    /* Horizontal navigation tabs for mobile */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        overflow-x: auto;
        white-space: nowrap;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .positive {
        color: #00ff00;
    }
    
    .negative {
        color: #ff4444;
    }
    
    /* Responsive grid */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            flex-direction: row;
        }
    }
    
    /* Full-screen modal styling */
    .modal-content {
        padding: 2rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    
    /* Header styling */
    .dashboard-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


# Initialize data sources
@st.cache_resource
def get_data_fetcher():
    """Initialize and cache data fetcher."""
    alpha_vantage_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    return NSEDataFetcher(alpha_vantage_key=alpha_vantage_key)


@st.cache_resource
def get_mock_data():
    """Initialize and cache mock data generator."""
    return MockNSEData(seed=42)


# Initialize session state
if 'data_source' not in st.session_state:
    st.session_state.data_source = 'mock'
if 'selected_stock' not in st.session_state:
    st.session_state.selected_stock = 'RELIANCE'


def create_line_chart(data, title, x_col, y_col):
    """Create an interactive Plotly line chart."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data[x_col],
        y=data[y_col],
        mode='lines+markers',
        name=title,
        line=dict(color='#667eea', width=3),
        marker=dict(size=6)
    ))
    fig.update_layout(
        title=title,
        xaxis_title=x_col.upper(),
        yaxis_title=y_col.upper(),
        hovermode='x unified',
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig


def create_candlestick_chart(data, title):
    """Create an interactive Plotly candlestick chart."""
    fig = go.Figure(data=[go.Candlestick(
        x=data['date'],
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name=title
    )])
    fig.update_layout(
        title=title,
        yaxis_title='Price (₹)',
        xaxis_title='Date',
        template='plotly_white',
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis_rangeslider_visible=False
    )
    return fig


def create_bar_chart(data, x_col, y_col, title, color_col=None):
    """Create an interactive Plotly bar chart."""
    if color_col:
        colors = ['green' if val > 0 else 'red' for val in data[color_col]]
    else:
        colors = '#667eea'
    
    fig = go.Figure(data=[
        go.Bar(x=data[x_col], y=data[y_col], marker_color=colors)
    ])
    fig.update_layout(
        title=title,
        xaxis_title=x_col.upper(),
        yaxis_title=y_col.upper(),
        template='plotly_white',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig


def display_metric_card(label, value, change=None):
    """Display a metric in a styled card."""
    change_html = ""
    if change is not None:
        change_class = "positive" if change >= 0 else "negative"
        change_symbol = "▲" if change >= 0 else "▼"
        change_html = f'<div class="{change_class}">{change_symbol} {abs(change):.2f}%</div>'
    
    st.markdown(f"""
    <div class="metric-card">
        <div style="font-size: 0.9rem; opacity: 0.9;">{label}</div>
        <div style="font-size: 2rem; font-weight: bold;">{value}</div>
        {change_html}
    </div>
    """, unsafe_allow_html=True)


def display_market_overview():
    """Display market overview with major indices and market movers."""
    st.markdown('<div class="dashboard-header"><h1>📈 Market Overview</h1></div>', 
                unsafe_allow_html=True)
    
    # Get data source
    mock = get_mock_data()
    
    # Major Indices
    st.subheader("Major Indices")
    market_summary = mock.get_market_summary()
    
    cols = st.columns(2)
    idx = 0
    for index_name, index_data in market_summary.items():
        if index_name not in ['source', 'note']:
            with cols[idx % 2]:
                display_metric_card(
                    index_name,
                    f"₹{index_data['value']:,.2f}",
                    index_data['change_percent']
                )
            idx += 1
    
    st.divider()
    
    # Top Movers
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚀 Top Gainers")
        gainers_losers = mock.get_top_gainers_losers(count=5)
        
        for stock in gainers_losers['gainers']:
            st.markdown(f"""
            **{stock['symbol']}** | ₹{stock['price']:.2f}  
            <span class="positive">▲ {stock['change_percent']:+.2f}%</span>
            """, unsafe_allow_html=True)
            st.divider()
    
    with col2:
        st.subheader("📉 Top Losers")
        
        for stock in gainers_losers['losers']:
            st.markdown(f"""
            **{stock['symbol']}** | ₹{stock['price']:.2f}  
            <span class="negative">▼ {stock['change_percent']:+.2f}%</span>
            """, unsafe_allow_html=True)
            st.divider()
    
    st.divider()
    
    # 52-Week High/Low
    st.subheader("📊 52-Week Highlights")
    
    # Generate sample 52-week data
    sample_stocks = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK']
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**52-Week High**")
        for symbol in sample_stocks[:3]:
            quote = mock.get_stock_quote(symbol)
            if 'error' not in quote:
                high_52w = quote['price'] * 1.15  # Mock 52-week high
                st.write(f"**{symbol}**: ₹{high_52w:.2f}")
    
    with col2:
        st.markdown("**52-Week Low**")
        for symbol in sample_stocks[:3]:
            quote = mock.get_stock_quote(symbol)
            if 'error' not in quote:
                low_52w = quote['price'] * 0.85  # Mock 52-week low
                st.write(f"**{symbol}**: ₹{low_52w:.2f}")
    
    st.divider()
    
    # Surprise Stocks
    st.subheader("⚡ Surprise Stocks of the Day")
    surprise_stocks = mock.get_top_gainers_losers(count=3)
    
    cols = st.columns(3)
    for idx, stock in enumerate(surprise_stocks['gainers'][:3]):
        with cols[idx]:
            st.metric(
                label=stock['symbol'],
                value=f"₹{stock['price']:.2f}",
                delta=f"{stock['change_percent']:+.2f}%"
            )
    
    st.divider()
    
    # Market News (Placeholder)
    st.subheader("📰 Market News")
    st.info("🔔 **Latest**: Markets show strong recovery with IT sector leading gains.")
    st.info("📈 **Trending**: Banking stocks gain momentum ahead of RBI policy meeting.")
    st.info("🌍 **Global**: Asian markets rally on positive US economic data.")
    
    st.divider()
    
    # Global Markets
    st.subheader("🌍 Global Markets")
    
    global_markets = {
        'S&P 500': {'value': 5127.50, 'change': 0.85},
        'NASDAQ': {'value': 16240.30, 'change': 1.20},
        'FTSE 100': {'value': 7952.60, 'change': -0.35},
        'Nikkei 225': {'value': 40125.25, 'change': 0.65},
        'Hang Seng': {'value': 17850.40, 'change': -0.15}
    }
    
    cols = st.columns(len(global_markets))
    for idx, (market, data) in enumerate(global_markets.items()):
        with cols[idx]:
            st.metric(
                label=market,
                value=f"{data['value']:,.2f}",
                delta=f"{data['change']:+.2f}%"
            )


def display_stock_analysis():
    """Display detailed stock analysis with charts."""
    st.subheader("📊 Stock Analysis")
    
    mock = get_mock_data()
    
    # Stock selector
    available_stocks = list(mock.STOCK_DATA.keys())
    selected_stock = st.selectbox(
        "Select Stock",
        available_stocks,
        index=available_stocks.index(st.session_state.selected_stock) 
        if st.session_state.selected_stock in available_stocks else 0
    )
    st.session_state.selected_stock = selected_stock
    
    # Get stock data
    quote = mock.get_stock_quote(selected_stock)
    historical = mock.get_historical_data(selected_stock, days=30)
    
    if 'error' not in quote:
        # Display current price
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Current Price", f"₹{quote['price']:.2f}", 
                     f"{quote['change_percent']:+.2f}%")
        with col2:
            st.metric("Open", f"₹{quote['open']:.2f}")
        with col3:
            st.metric("High", f"₹{quote['high']:.2f}")
        with col4:
            st.metric("Low", f"₹{quote['low']:.2f}")
        
        # Historical data chart
        if 'error' not in historical:
            df = pd.DataFrame(historical['data'])
            
            # Candlestick chart
            st.plotly_chart(
                create_candlestick_chart(df, f"{selected_stock} - 30 Day Price Movement"),
                use_container_width=True
            )
            
            # Volume chart
            fig_volume = create_bar_chart(
                df, 'date', 'volume', 
                f"{selected_stock} - Trading Volume"
            )
            st.plotly_chart(fig_volume, use_container_width=True)
            
            # Price trend
            fig_price = create_line_chart(
                df, f"{selected_stock} - Closing Price Trend",
                'date', 'close'
            )
            st.plotly_chart(fig_price, use_container_width=True)


def display_portfolio():
    """Display portfolio tracking."""
    st.subheader("💼 Portfolio")
    
    mock = get_mock_data()
    
    # Sample portfolio
    portfolio_data = {
        'Symbol': ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK'],
        'Quantity': [50, 30, 100, 40, 80]
    }
    
    portfolio_list = []
    total_value = 0
    
    for symbol, qty in zip(portfolio_data['Symbol'], portfolio_data['Quantity']):
        quote = mock.get_stock_quote(symbol)
        if 'error' not in quote:
            value = quote['price'] * qty
            total_value += value
            portfolio_list.append({
                'Symbol': symbol,
                'Quantity': qty,
                'Price': quote['price'],
                'Value': value,
                'Change %': quote['change_percent']
            })
    
    # Display total value
    st.metric("Total Portfolio Value", f"₹{total_value:,.2f}")
    
    # Display portfolio table
    df = pd.DataFrame(portfolio_list)
    st.dataframe(
        df.style.format({
            'Price': '₹{:.2f}',
            'Value': '₹{:,.2f}',
            'Change %': '{:+.2f}%'
        }),
        use_container_width=True
    )
    
    # Portfolio distribution pie chart
    fig = px.pie(
        df, 
        values='Value', 
        names='Symbol',
        title='Portfolio Distribution',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(fig, use_container_width=True)


def display_watchlist():
    """Display stock watchlist."""
    st.subheader("👁️ Watchlist")
    
    mock = get_mock_data()
    
    # Sample watchlist
    watchlist = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK', 
                 'HINDUNILVR', 'ITC', 'SBIN']
    
    watchlist_data = []
    for symbol in watchlist:
        quote = mock.get_stock_quote(symbol)
        if 'error' not in quote:
            watchlist_data.append({
                'Symbol': symbol,
                'Price': quote['price'],
                'Change': quote['change'],
                'Change %': quote['change_percent'],
                'Volume': quote['volume']
            })
    
    df = pd.DataFrame(watchlist_data)
    st.dataframe(
        df.style.format({
            'Price': '₹{:.2f}',
            'Change': '₹{:+.2f}',
            'Change %': '{:+.2f}%',
            'Volume': '{:,}'
        }),
        use_container_width=True
    )


def display_settings():
    """Display settings page."""
    st.subheader("⚙️ Settings")
    
    st.write("### Data Source")
    data_source = st.radio(
        "Select data source:",
        ['Mock Data (Demo)', 'Live Data (Yahoo Finance)'],
        index=0 if st.session_state.data_source == 'mock' else 1
    )
    st.session_state.data_source = 'mock' if 'Mock' in data_source else 'live'
    
    st.write("### Display Preferences")
    st.checkbox("Show volume in charts", value=True)
    st.checkbox("Enable notifications", value=False)
    st.selectbox("Theme", ['Light', 'Dark', 'Auto'])
    
    st.write("### API Configuration")
    st.info("API keys are configured via environment variables for security.")
    st.code("""
# Set environment variables in Cloud Run:
ALPHA_VANTAGE_API_KEY=your_key_here
FMP_API_KEY=your_key_here
    """)
    
    st.write("### About")
    st.write("**ATS-NSE Stock Market Analysis Suite**")
    st.write("Version: 1.0.0")
    st.write("Developed by: Mandar Bahadarpurkar")


def display_help():
    """Display help page."""
    st.subheader("❓ Help & Documentation")
    
    st.write("### Getting Started")
    st.write("""
    1. **Market Overview**: View major indices, top movers, and market news
    2. **Stock Analysis**: Analyze individual stocks with interactive charts
    3. **Portfolio**: Track your holdings and performance
    4. **Watchlist**: Monitor your favorite stocks
    """)
    
    st.write("### Navigation")
    st.write("""
    - Use the tabs at the top to switch between sections
    - On mobile: Swipe horizontally through tabs
    - On desktop: Click tabs or use hamburger menu for additional options
    """)
    
    st.write("### Data Sources")
    st.write("""
    - **Mock Data**: Realistic simulated data for demonstration
    - **Live Data**: Real-time data from Yahoo Finance (no API key needed)
    - **Premium APIs**: Alpha Vantage, FMP (requires API keys)
    """)
    
    st.write("### Support")
    st.write("For issues or questions, visit: https://github.com/mandarab76/ATS-NSE-Stock-Suite")


def main():
    """Main dashboard application."""
    # Header
    st.markdown("""
    <div class="dashboard-header">
        <h1>📈 ATS-NSE Stock Market Suite</h1>
        <p>Real-time NSE Stock Analysis & Portfolio Management</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hamburger menu in sidebar
    with st.sidebar:
        st.title("📱 Menu")
        menu_option = st.radio(
            "Navigation",
            ["Market Overview", "Stock Analysis", "Portfolio", "Watchlist", 
             "Settings", "Help"],
            label_visibility="collapsed"
        )
    
    # Main content area with horizontal tabs for mobile
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏠 Overview", "📊 Analysis", "💼 Portfolio", 
        "👁️ Watch", "⚙️ Settings", "❓ Help"
    ])
    
    with tab1:
        display_market_overview()
    
    with tab2:
        display_stock_analysis()
    
    with tab3:
        display_portfolio()
    
    with tab4:
        display_watchlist()
    
    with tab5:
        display_settings()
    
    with tab6:
        display_help()
    
    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <small>Last updated: {}</small><br>
        <small>Data source: {}</small><br>
        <small>© 2024 ATS-NSE Stock Suite | Developed by Mandar Bahadarpurkar</small>
    </div>
    """.format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Mock Data (Demo)" if st.session_state.data_source == 'mock' else "Live Data"
    ), unsafe_allow_html=True)


if __name__ == "__main__":
    main()
