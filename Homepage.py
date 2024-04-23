import streamlit as st

st.set_page_config(page_title="ROI Calculator", page_icon=":moneybag:")


# Main function to switch between pages
def main():
    st.title("Instructions")

    st.write("Welcome to the ROI Calculator app!")
    st.write("Use the sidebar to navigate between different pages.")

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

    st.markdown("#### How is the ROI calculated?")
    st.latex(
        r"""
        \text{ROI} = \frac{\text{Revenue BDP Order} - \text{Revenue Phone Order}}{\text{Revenue Phone Order}} \times 100
        """
    )

    st.markdown("## Calculator V2")


if __name__ == "__main__":
    main()
