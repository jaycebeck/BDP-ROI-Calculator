import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="ROI Calculator", page_icon=":chart_with_upwards_trend:")


def calculatorV3():
    st.title("BulkDelivery PRO Profit Calculator")

    st.write(
        "BulkDelivery PRO is a service that allows for their customers to seamlessly integrate online ordering to their bulk delivery goods such as a gravel, soil or mulch. "
        "This calculator helps you estimate the profit you can make by using BulkDelivery PRO. "
        "You can adjust the variables below to see how much profit you can make by using BulkDelivery PRO."
    )

    explanation_on = st.toggle("Show Variable Explanations")

    if explanation_on:
        st.markdown(
            "- **Average sale price** is the average price of an order you currently make. "
        )
        st.write(
            "- **Average number of orders per day** is the average number of orders you currently make in a day. "
        )
        st.write(
            "- **Average time to take an order** is the average time it takes to take an order over the phone. "
        )
        st.write(
            "- **Average time to organize delivery** is the average time it takes to organize delivery with a driver. "
        )
        st.write(
            "- **Number of order handlers** is the number of employees taking orders. "
        )
        st.write(
            "- **Order handler hourly wage** is the hourly wage of the employees taking orders. "
        )
        st.write(
            "- **Conversion rate** is the percentage of sales that will be online when first implementing Bulk Delivery Pro. "
            "See what 100% online sales would look like by setting the conversion rate to 1.0."
        )
        st.write(
            "- **Commission Cost Given to Customers** is toggle to give a fee to customers to remove commission from the business's expense to use BulkDelivery PRO."
        )

    avg_sale_price = st.slider(
        "Average sale price you currently make on orders:",
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
        "Average time to organize delivery with a driver (minutes):",
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

    conversion_to_online = st.slider(
        "Conversion rate to online orders:",
        min_value=0.0,
        value=0.33,
        max_value=1.0,
        step=0.01,
    )

    comm_to_cust = st.checkbox("Comission Cost Given to Customers")

    # Calculate ROI
    if st.button("Calculate Profit"):

        commission_rate = 0.025
        employee_overhead = 1.3

        st.title("Monthly Business States")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Basic Ordering System(Phone Orders)")
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
            st.write(f"Cost of Employee to take Orders: ${current_employee_cost:.2f}")

            # Current Profit
            current_profit = current_sales - current_employee_cost
            st.write(f"Profit: ${current_profit:.2f}")

        with col2:
            st.subheader("Add Online Ordering with BulkDelivery PRO")
            new_orders_online = np.round(avg_num_orders * conversion_to_online)
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
                * (1 - conversion_to_online)
                * 22
                * avg_num_orders
            )

            st.write(f"Cost of Employee to take Orders: ${new_employee_cost:.2f}")

            # BulkDelivery PRO Commission
            commission = new_orders_online * avg_sale_price * commission_rate * 30

            # New Profit depending on if commission is given to customers
            if comm_to_cust:
                new_profit = new_sales - new_employee_cost
                st.write(f"Commission Cost to Business: ${0.0}")
            else:
                new_profit = new_sales - new_employee_cost - commission
                st.write(f"Commission Cost to Business: ${commission:.2f}")
            st.write(f"Profit: ${new_profit:.2f}")


            st.write("**Positive Profit Difference**: ${:.2f}".format(new_profit - current_profit))

        df = pd.DataFrame(
            {
                "Profit": [np.round(current_profit, 2), np.round(new_profit, 2)],
            },
            index=["Current", "~BulkDelivery PRO"],
        )
        st.bar_chart(data=df, height=400)


if __name__ == "__main__":
    calculatorV3()
