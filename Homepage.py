import streamlit as st

st.set_page_config(page_title="ROI Calculator", page_icon=":chart_with_upwards_trend:")


# Main function to switch between pages
def main():
    st.title("Calculations")
    st.markdown("## Calculator V1")

    st.markdown("#### How are the costs of BulkDelivery PRO calculated?")

    st.latex(r""" \text{Commission Rate} = 2.5\% """)
    st.latex(
        r"""
        \text{Cost of BulkDelivery PRO} = \text{Average Sale Price} \times \text{Commission Rate}
        """
    )

    st.latex(
        r""" \text{Cost of Phone Orders} = (\text{Time to Take Order} + \text{Time to Relay Order to Driver}) \times \text{Average Wage} """
    )

    st.latex(
        r"""
        \text{Revenue Phone Orders} = \text{Average Sale Price} - \text{Cost of Phone Orders}
        """
    )

    st.latex(
        r"""
        \text{Revenue BDP Order} = \text{Average Sale Price} - \text{Cost of BulkDelivery PRO}
        """
    )

    st.markdown("#### How is the ROI calculated?")
    st.latex(
        r"""
        \text{ROI} = \frac{\text{Revenue BDP Order} - \text{Revenue Phone Order}}{\text{Revenue Phone Order}} \times 100
        """
    )

    st.markdown("## Calculator V2")
    st.latex(r""" \text{Commission Rate} = 2.5\% """)
    st.latex(
        r"""
        \text{BDP Number of Orders} = (\text{Average Number of Orders} \times 1.2 \text{*}))
        """
    )

    st.latex(
        r"""
        \text{Cost of BulkDelivery PRO} = \text{BDP Number of Orders} \times \text{Average Sale Price} \times \text{Commission Rate}
        """
    )

    st.latex(
        r""" \text{Cost of Phone Orders} = \frac{\text{Number of Order Takers} \times ((\text{Time to Take Order} + \text{Time to Relay Order to Driver}) \times \text{Average Wage})}{\text{Average Number of Orders}} """
    )

    st.latex(
        r"""
        \text{Revenue Phone Orders} = (\text{Average Sale Price} \times \text{Average Number of Orders}) - \text{Cost of Phone Orders}
        """
    )

    st.latex(
        r"""
        \text{Revenue BDP Orders} = (\text{Average Sale Price} \times \text{BDP Number of Orders}) - \text{Cost of BulkDelivery PRO}
        """
    )

    st.write("*1.2 being a 20% daily sales increase due to the online ordering system")

    st.markdown("#### How is the ROI calculated?")
    st.latex(
        r"""
        \text{ROI} = \frac{\text{Revenue BDP Orders} - \text{Revenue Phone Orders}}{\text{Revenue Phone Orders}} \times 100
        """
    )


if __name__ == "__main__":
    main()
