# 💼 Subscription Plans
if menu == "💼 Subscription Plans":
    st.subheader("💼 Subscription Tiers")

    st.markdown("""
    <style>
        .sub-table th, .sub-table td {
            padding: 10px;
            text-align: center;
        }
        .sub-table th {
            background-color: #f0f2f6;
        }
        .sub-table {
            border-collapse: collapse;
            width: 100%;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .sub-table, .sub-table td, .sub-table th {
            border: 1px solid #ddd;
        }
    </style>

    <table class="sub-table">
        <tr>
            <th>Features</th>
            <th>🟢 Basic (₹0)</th>
            <th>🔵 Premium (₹499)</th>
            <th>🔴 Elite (₹999)</th>
        </tr>
        <tr>
            <td>Study Partner Matching</td>
            <td>✅</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Access to Notes & Materials</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Teacher Access</td>
            <td>❌</td>
            <td>Optional</td>
            <td>✅ Free 3 Sessions</td>
        </tr>
        <tr>
            <td>Job Placement Assistance</td>
            <td>❌</td>
            <td>❌</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Priority Matching</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅</td>
        </tr>
        <tr>
            <td>Motivational Reminders & Progress Tracking</td>
            <td>❌</td>
            <td>✅</td>
            <td>✅ + Personalized Insights</td>
        </tr>
        <tr>
            <td>Support</td>
            <td>Email Only</td>
            <td>Live Chat</td>
            <td>Live Chat + Phone Support</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Choose Basic Plan (₹0)"):
            st.session_state.selected_plan = "Basic"
    with col2:
        if st.button("Choose Premium Plan (₹499)"):
            st.session_state.selected_plan = "Premium"
    with col3:
        if st.button("Choose Elite Plan (₹999)"):
            st.session_state.selected_plan = "Elite"

    if st.session_state.selected_plan:
        st.markdown(f"### Proceed to Payment for **{st.session_state.selected_plan} Plan**")
        method = st.radio("Choose Payment Method", ["UPI", "Credit/Debit Card", "PayPal"])
        if method == "UPI":
            st.text_input("Enter UPI ID")
        elif method == "Credit/Debit Card":
            st.text_input("Card Number")
            st.text_input("Card Holder Name")
            st.text_input("Expiry Date (MM/YY)")
            st.text_input("CVV")
        elif method == "PayPal":
            st.text_input("PayPal Email")
        if st.button("Pay Now"):
            st.success(f"✅ Payment successful for {st.session_state.selected_plan} Plan!")
