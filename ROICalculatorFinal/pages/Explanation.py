import streamlit as st

st.set_page_config(page_title="Bulk Delivery PRO Calculator", page_icon=":chart_with_upwards_trend:")


# Main function to switch between pages
def main():
    st.markdown("## Variable Definitions:")
    st.latex(r""" C = \text{Commission Rate} = 2.5\% """)
    st.latex(r""" S = \text{Average Sale Price}""")
    st.latex(r""" O = \text{Daily Average Number of Orders}""")
    st.latex(
        r""" T = \text{Average Time to Take Order} + \text{Average Time to Organize Order}"""
    )
    st.latex(r""" W = \text{Number of Order Handlers}""")
    st.latex(r""" H = \text{Order Handler Hourly Wage}""")
    st.latex(r""" E = \text{Employee Overhead}""")
    st.latex(r""" M = \text{Online Conversion Rate}""")

    st.markdown("## Calculations:")

    st.markdown("### Phone Sales:")

    st.latex(
        r"""
        \text{Phone Sales Revenue} = S \times O \times \text{22 days}^1
        """
    )
    st.latex(
        r"""
    \text{Employee Cost} = W \times T \times H \times E \times O \times \text{22 days}^1
    """
    )

    st.latex(
        r"""
    \text{Total Phone Sales Profit} = \text{Phone Sales Revenue} - \text{Cost of Phone Orders}
    """
    )

    st.markdown("### Adding BulkDelivery Pro Sales:")

    st.latex(
        r"""
        \text{Number Online Orders} = O \times M
        """
    )
    st.latex(
        r"""
        \text{Number Phone Orders} = O - \text{Number Online Orders}
        """
    )

    st.latex(
        r"""
        \text{BulkDelivery PRO Revenue} = \text{Number Phone Orders} \times S \times \text{22 days}^1 + \text{Number Online Orders} \times S \times \text{30 days}^2
        """
    )

    st.latex(
        r"""
        \text{Employee Cost with BulkDelivery Pro}^3 = \text{Employee Cost} \times (1 - \text{M})
        """
    )

    st.latex(
        r"""
        \text{BulkDelivery Pro Commision Cost} = \text{Number Online Orders} \times C \times \text{30 days}^2
        """
    )

    st.markdown("##### if commision(C) is given to customers:")
    st.latex(
        r"""
        \text{Total BulkDelivery PRO Profit} = \text{BulkDelivery Pro Revenue} - \text{Employee Cost with BulkDelivery Pro}
        """
    )
    st.markdown("##### if commision(C) is *NOT* given to customers:")
    st.latex(
        r"""
        \text{Total BulkDelivery PRO Profit} = \text{Total BulkDelivery PRO Profit} - \text{BulkDelivery Pro Commision Cost}
        """
    )

    st.markdown("### Assumptions:")
    st.markdown(
        "1. Assuming the number of days an employee works to answer phones in a month is 22."
    )
    st.markdown(
        "2. Assuming online orders allows for 30 days of sales."
    )
    st.markdown(
        "3. Assuming that at 100% online orders, the number of employees working on orders is 0. "
        "At 0% online orders, the number of employees working on orders is the same as the number of phone orders."
    )
    st.write(
        "- Employee Overhead is the cost of benefits, insurance, etc. per employee"
    )


if __name__ == "__main__":
    main()
