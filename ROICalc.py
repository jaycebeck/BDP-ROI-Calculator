import streamlit as st


commission_rate = 0.025


# Function to calculate ROI
def calculate_roi(cost, gain):
    roi = ((gain - cost) / cost) * 100
    return roi


def calculate_customer_cost(
    num_office_workers,
    avg_worker_wage,
    avg_time_to_take_order,
    total_orders,
    avg_time_organize_delivery,
):
    time_to_take_orders = (
        (avg_time_to_take_order + avg_time_organize_delivery) * total_orders / 60
    )
    cost_of_workers = num_office_workers * avg_worker_wage * time_to_take_orders
    return cost_of_workers


def calculate_bdp_cost(avg_sale_price, total_orders):
    total_orders = total_orders + (total_orders * 1.02)
    cost_of_orders = total_orders * avg_sale_price
    bdp_cost = cost_of_orders * commission_rate
    return bdp_cost


# Streamlit app
def main():
    # App title
    st.title("BulkDelivery PRO ROI Calculator")

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

        cost_cust = calculate_customer_cost(
            num_office_workers,
            avg_worker_wage,
            avg_time_to_take_order,
            total_orders,
            avg_time_organize_delivery,
        )

        bdp_cost = calculate_bdp_cost(avg_sale_price, total_orders)

        gain = cost_cust - bdp_cost

        roi = calculate_roi(cost_cust, gain)
        st.write(f"Customer Cost: ${cost_cust:.2f}")
        st.write(f"BDP Cost: ${bdp_cost:.2f}")
        st.write(f"Gain: ${gain:.2f}")
        st.write(f"ROI: {roi:.2f}%")


# Run the app
if __name__ == "__main__":
    main()
