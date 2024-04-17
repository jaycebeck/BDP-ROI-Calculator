import streamlit as st


commission_rate = 0.025


def calculate_customer_cost(
    num_office_workers,
    avg_worker_wage,
    avg_time_to_take_order,
    total_orders,
    avg_time_organize_delivery,
):
    cost = (
        num_office_workers
        * (avg_time_organize_delivery + avg_time_to_take_order)
        * avg_worker_wage
        / total_orders
        / 60
    )
    return cost


def calculate_bdp_cost(avg_sale_price, total_orders):
    cost_of_orders = total_orders * avg_sale_price
    bdp_cost = cost_of_orders * commission_rate
    return bdp_cost


def sales(total_orders, avg_sale_price):
    return total_orders * avg_sale_price


# Streamlit app
def main():
    # App title
    st.title("BulkDelivery PRO ROI Calculator")

    st.markdown(
        "BulkDelivery PRO is a service that allows you to take orders online and have them delivered to your customers. "
        "This calculator helps you determine the return on investment of using BulkDelivery PRO."
    )

    st.markdown("#### How are the costs of BulkDelivery PRO calculated?")

    st.latex(
        r"""
        \text{Cost of BulkDelivery PRO} = \text{Total Orders} \times \text{Average Sale Price} \times \text{Commission Rate}
        """
    )

    st.latex(r""" \text{Commission Rate} = 2.5\% """)

    st.latex(
        r""" \text{Cost of Phone Orders} = \text{Number of Phone Receptionists} \times (\text{Time to Take Order} + \text{Time to Relay Order to Driver}) \times \text{Average Wage} \div \text{Total Orders} \div 60"""
    )

    st.latex(
        r""" \text{Sales} = \text{Total Orders} \times \text{Average Sale Price} """
    )

    st.markdown("#### How is the ROI calculated?")
    st.latex(
        r"""
        \text{ROI} = \frac{(\text{Sales} - \text{Cost of BDP}) - (\text{Sales} - \text{Phone Ordering})}{\text{Sales} - \text{Phone Ordering}} \times 100
        """
    )

    # User inputs
    num_office_workers = st.slider(
        "Number of people that take orders:",
        min_value=0,
        value=3,
        max_value=20,
        step=1,
    )

    avg_time_to_take_order = st.slider(
        "Average time to take an order (minutes):",
        min_value=0,
        value=5,
        max_value=20,
        step=1,
    )

    avg_worker_wage = st.slider(
        "Hourly wage of someone that takes orders:",
        min_value=7.25,
        value=16.25,
        max_value=30.0,
        step=0.25,
    )

    avg_number_orders = st.slider(
        "Average number of orders taken per day:",
        min_value=0,
        value=5,
        max_value=20,
        step=1,
    )

    avg_sale_price = st.slider(
        "Average sale price:",
        min_value=0,
        value=500,
        max_value=1000,
        step=10,
    )

    avg_time_organize_delivery = st.slider(
        "Average time to organize delivery (minutes):",
        min_value=0,
        value=10,
        max_value=30,
        step=1,
    )
    # Calculate ROI
    if st.button("Calculate ROI"):

        total_orders = num_office_workers * avg_number_orders

        sales1 = sales(total_orders, avg_sale_price)

        cost_cust = sales1 - (
            calculate_customer_cost(
                num_office_workers,
                avg_worker_wage,
                avg_time_to_take_order,
                total_orders,
                avg_time_organize_delivery,
            )
        )

        bdp_cost = sales1 - calculate_bdp_cost(avg_sale_price, total_orders)

        gain = cost_cust - bdp_cost

        roi = (gain / cost_cust) * 100
        st.write(f"Customer Cost: ${cost_cust:.2f}")
        st.write(f"BDP Cost: ${bdp_cost:.2f}")
        st.write(f"Gain: ${gain:.2f}")
        st.write(f"ROI: {roi:.2f}%")


# Run the app
if __name__ == "__main__":
    main()
