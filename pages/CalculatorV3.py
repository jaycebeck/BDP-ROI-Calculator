import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="ROI Calculator", page_icon=":chart_with_upwards_trend:")


def calculatorV3():
    st.title("BulkDelivery PRO ROI Calculator V3")

    avg_sale_price = st.slider(
        "Average sale price:",
        min_value=150,
        value=300,
        max_value=800,
        step=10,
    )

    avg_num_orders = st.slider(
        "Average number of orders per day:",
        min_value=6,
        value=8,
        max_value=20,
        step=1,
    )

    avg_time_to_take_order = st.slider(
        "Average time to take a phone order (minutes):",
        min_value=4,
        value=5,
        max_value=20,
        step=1,
    )

    avg_time_organize_delivery = st.slider(
        "Average time to organize delivery with driver (minutes):",
        min_value=5,
        value=10,
        max_value=30,
        step=1,
    )

    people_taking_orders = st.slider(
        "Number of order handlers taking orders:",
        min_value=1,
        value=2,
        max_value=5,
        step=1,
    )

    avg_worker_wage = st.slider(
        "Order handler hourly wage:",
        min_value=16.0,
        value=22.0,
        max_value=30.0,
        step=0.25,
    )

    avg_product_margin = (
        st.slider(
            "Average product margin (%):",
            min_value=5,
            value=10,
            max_value=20,
            step=1,
        )
        / 100
    )

    comm_to_cust = st.checkbox("Comission Cost Given to Customers")

    # Calculate ROI
    if st.button("Calculate Profit"):

        commission_rate = 0.025
        employee_overhead = 1.3

        st.title("Monthly Business States")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Current State")
            # Current Sales
            current_sales = avg_sale_price * avg_num_orders * 22
            st.write(f"Sales: ${current_sales:.2f}")

            # Current Employee Cost
            current_employee_cost = (
                avg_worker_wage
                * employee_overhead
                / 60
                * (avg_time_organize_delivery + avg_time_to_take_order)
                * people_taking_orders
                * 22
                * avg_num_orders
            )
            st.write(f"Employee Cost to take Orders: ${current_employee_cost:.2f}")

            # Current Cost of Goods Sold
            current_cost_of_goods_sold = (
                avg_sale_price * avg_num_orders * avg_product_margin
            )
            st.write(f"Cost of Goods Sold: ${current_cost_of_goods_sold:.2f}")

            # Current Profit
            current_profit = (
                current_sales - current_cost_of_goods_sold - current_employee_cost
            )
            st.write(f"Profit: ${current_profit:.2f}")

        with col2:
            st.subheader("State with BulkDelivery PRO")
            new_orders_online = np.round(avg_num_orders * (1 / 3))
            new_orders_phone = avg_num_orders - new_orders_online

            # New Sales
            new_sales = (
                avg_sale_price * (new_orders_phone) * 22
                + new_orders_online * avg_sale_price * 30
            )
            st.write(f"Sales: ${new_sales:.2f}")

            # New Employee Cost assuming number of employees is halved
            new_employee_cost = (
                avg_worker_wage
                * employee_overhead
                / 60
                * (avg_time_organize_delivery + avg_time_to_take_order)
                * people_taking_orders
                / 2
                * 22
                * avg_num_orders
            )

            st.write(f"Employee Cost to take Orders: ${new_employee_cost:.2f}")

            # New Cost of Goods Sold
            new_cost_of_goods_sold = (
                avg_sale_price * (avg_num_orders) * avg_product_margin
            )
            st.write(f"Cost of Goods Sold: ${new_cost_of_goods_sold:.2f}")

            # BulkDelivery PRO Commission
            commission = new_orders_online * commission_rate * 30

            # New Profit depending on if commission is given to customers
            if comm_to_cust:
                new_profit = new_sales - new_cost_of_goods_sold - new_employee_cost
            else:
                new_profit = (
                    new_sales - new_cost_of_goods_sold - new_employee_cost - commission
                )
            st.write(f"Profit: ${new_profit:.2f}")

        df = pd.DataFrame(
            {
                # "Cost of Goods Sold": [
                #     current_cost_of_goods_sold,
                #     new_cost_of_goods_sold,
                # ],
                # "Employee Cost": [current_employee_cost, new_employee_cost],
                # "BulkDelivery PRO Commission": [0, commission],
                "Profit": [np.round(current_profit, 2), np.round(new_profit, 2)],
            },
            index=["Current", "~BulkDelivery PRO"],
        )
        st.bar_chart(data=df, height=400)

        # st.markdown("### Assumptions")
        # st.write(
        #     "1. The average sale price is the same for both the current state and the BulkDelivery PRO state."
        # )
        # st.write(
        #     "2. The average number of orders per day is the same for both the current state and the BulkDelivery PRO state but a 1/3 of orders are being placed outside of working hours."
        # )


if __name__ == "__main__":
    calculatorV3()
