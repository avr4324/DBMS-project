import streamlit as st
from backend1 import insertPerson, insertHospital, insertInventory, addSupplies, newVaccination, getPatients, getHospitals, getInventory, fetch_person_ids, fetch_hospital_ids, fetch_inventory_ids, getSupplies, getVaccination, insertVaccine, update_function, delete_function, select_function, insert_doctors,getDoctors
from datetime import datetime


# Initialize session state variables to keep track of navigation
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Function to switch between pages
def switch_page(page):
    st.session_state.page = page

# Main page with buttons
def main_page():
    st.title("Covid Vaccine Management System")
    st.write("Click a button to navigate to another page.")
    st.markdown("---")

    button_style = """
        <style>
            .stButton > button {
                margin: 10px;
                padding: 10px 20px;
                border-radius: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                font-size: 16px;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Add patients"):
            switch_page('patients_page')
        if st.button("Add Hospital"):
            switch_page('hospital_page')
        if st.button("Add Inventory"):
            switch_page('inventory_page')
        if st.button("Add Supplies"):
            switch_page('supplies_page')
        if st.button("Add Vaccination"):
            switch_page('vaccination_page')
        if st.button("Add Vaccine"):
            switch_page('vaccine_page')
        if st.button("Add Doctor"):
            switch_page('doctor_page')
    
    with col2:
        
        if st.button("Update"):
            switch_page('update')
        if st.button("Delete"):
            switch_page('delete')
        if st.button("Filter"):
            switch_page('filter')
    
    with col3:
        if st.button("Display Patients"):
            switch_page('display_patients')
        if st.button("Display Hospitals"):
            switch_page('display_hospitals')
        if st.button("Display Inventory"):
            switch_page('display_inventory')
        if st.button("Display Supplies"):
            switch_page('display_supplies')
        if st.button("Display Vaccination"):
            switch_page('display_vaccination')
        if st.button("Display Doctors"):
            switch_page('display_doctors')
    

# Form page with text fields and a submit button
def patients_page():
    st.title("Input Form Page")
    st.write("Fill in the details below and submit.")
    name = st.text_input("Name")
    options = ['male', 'female']
    gender = st.selectbox("Gender", options)
    selected_date = st.date_input('Date of Birth', datetime.now())
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    pincode = st.text_input("Pincode")
    area = st.text_input("Area")
    city = st.text_input("City")
    state = st.text_input("State")

    if st.button("Submit"):
        insertPerson(name, gender, selected_date, phone_number, pincode, email, area, city, state)
        st.success("Patient record inserted successfully")

    if st.button("Back to Main Page"):
        switch_page('main')

def insert_hospital_page():
    st.title("Insert Hospital Page")
    st.write("Fill in the details below and submit.")
    name = st.text_input("Hospital Name")
    pwd = st.text_input("Password", type="password")
    contactno = st.text_input("Contact Number")
    htype = st.selectbox("Type", ["G", "P"])
    pincode = st.text_input("Pincode")
    area = st.text_input("Area")
    city = st.text_input("City")
    state = st.text_input("State")
    email = st.text_input("Email")
    vac = st.selectbox("Vaccine", ["Covishield", "Covaxin", "Sputnik V"])
    quant_rem = st.text_input("Quantity Remaining")
    
    if st.button("Submit"):
        insertHospital(name, pwd, contactno, htype, pincode, area, city, state, email, vac, quant_rem)
        st.success("Hospital record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')

def inventory_page():
    st.title("Insert Inventory Page")
    st.write("Fill in the details below and submit.")
    name = st.text_input("Inventory Name")
    contactno = st.text_input("Contact Number")
    pincode = st.text_input("Pincode")
    area = st.text_input("Area")
    city = st.text_input("City")
    state = st.text_input("State")
    
    if st.button("Submit"):
        insertInventory(name, contactno, pincode, area, city, state)
        st.success("Inventory record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')

def supplies_page():
    st.title("Add Supplies Page")
    st.write("Fill in the details below and submit.")
    hospital_ids = fetch_hospital_ids()
    inventory_ids = fetch_inventory_ids()
    hospital_id = st.selectbox("Select Hospital ID:", hospital_ids)
    inventory_id = st.selectbox("Select Inventory ID:", inventory_ids)
    quantity = st.text_input("Quantity")
    selected_date = st.date_input('Select a date', datetime.today())
    selected_time = st.time_input('Select a time', datetime.now(),step=60)
    timestamp = f"{selected_date} {selected_time}"
    
    if st.button("Submit"):
        addSupplies(hospital_id, inventory_id, quantity, timestamp)
        st.success("Supplies record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')

def vaccination_page():
    st.title("New Vaccination Page")
    st.write("Fill in the details below and submit.")
    person_ids = fetch_person_ids()
    hospital_ids = fetch_hospital_ids()
    person_id = st.selectbox('Select Person ID:', person_ids)
    hospital_id = st.selectbox('Select Hospital ID:', hospital_ids)
    date_first = st.date_input("First Dose Date")
    date_second = st.date_input("Second Dose Date")

    
    if st.button("Submit"):
        newVaccination(person_id, hospital_id, date_first, date_second)
        st.success("Vaccination record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')

def vaccine_page():
    st.title("Vaccine Page")
    st.write("Fill in the details below and submit.")
    v_name = st.text_input("Vaccine Name")
    v_company = st.text_input("Company Name")   
    v_cost = st.text_input("Cost")
    
    if st.button("Submit"):
        insertVaccine(v_name, v_company, v_cost)
        st.success("Vaccine record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')
    
def doctor_page():
    st.title("Doctor Page")
    st.write("Fill in the details below and submit.")
    d_id = st.text_input("D_id")
    d_dept = st.selectbox("Department",['Cardiology','Neurology'])
    
    if st.button("Submit"):
        insert_doctors(d_id, d_dept)
        st.success("Doctor record inserted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')

def update():
    st.title("Update Page")
    st.write("Fill in the details below and submit.")
    table = st.selectbox("Table", ["Person", "Hospital", "Inventory", "Supplies", "Vaccinates", "Vaccine", "Doctor"])
    if table == "Person":
        attribute = st.selectbox("Attribute", ["p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        attribute = st.selectbox("Attribute", ["h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        attribute = st.selectbox("Attribute", ["i_name","i_contactno","i_address"])
    elif table == "Supplies":
        attribute = st.selectbox("Attribute", ["s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        attribute = st.selectbox("Attribute", ["hosp","date_first","date_second"])
    elif table == "Vaccine":
        attribute = st.selectbox("Attribute", ["v_name","v_company","v_cost"])
    elif table == "Doctor":
        attribute = st.selectbox("Attribute", ["d_dept"])
    
    new_value = st.text_input("New Value")
    if table == "Person":
        C_attribute = st.selectbox("Condition", ["p_id","p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        C_attribute = st.selectbox("Condition", ["h_id","h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        C_attribute = st.selectbox("Condition", ["i_id","i_name","i_contactno","i_address"])
    elif table == "Supplies":
        C_attribute = st.selectbox("Condition", ["s_id","s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        C_attribute = st.selectbox("Condition", ["p","hosp","date_first","date_second"])
    elif table == "Vaccine":
        C_attribute = st.selectbox("Condition", ["v_name","v_company","v_cost"])
    elif table == "Doctor":
        C_attribute = st.selectbox("Condition", ["d_id","d_dept"])

    op = st.selectbox("Operator", ["=", ">", "<", ">=", "<=", "!="])

    value = st.text_input("Value")

    condition = f"{C_attribute} {op} '{value}'"

    if st.button("Submit"):
        update_function(table, attribute, new_value, condition)
        st.success("Record updated successfully")
    if st.button("Back to Main Page"):
        switch_page('main')


def delete():
    st.title("Delete Page")
    st.write("Fill in the details below and submit.")
    table = st.selectbox("Table", ["Person", "Hospital", "Inventory", "Supplies", "Vaccinates", "Vaccine", "Doctor"])
    if table == "Person":
        C_attribute = st.selectbox("Attribute", ["p_id","p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        C_attribute = st.selectbox("Attribute", ["h_id","h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        C_attribute = st.selectbox("Attribute", ["i_id","i_name","i_contactno","i_address"])
    elif table == "Supplies":
        C_attribute = st.selectbox("Attribute", ["s_id","s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        C_attribute = st.selectbox("Attribute", ["p","hosp","date_first","date_second"])
    elif table == "Vaccine":
        C_attribute = st.selectbox("Attribute", ["v_name","v_company","v_cost"])
    elif table == "Doctor":
        C_attribute = st.selectbox("Attribute", ["d_id","d_dept"])

    op = st.selectbox("Operator", ["=", ">", "<", ">=", "<=", "!="])

    value = st.text_input("Value")

    condition = f"{C_attribute} {op} '{value}'"

    if st.button("Submit"):
        delete_function(table, condition)
        st.success("Record deleted successfully")
    if st.button("Back to Main Page"):
        switch_page('main')


def filter():   
    st.title("Filter Page")
    st.write("Fill in the details below and submit.")
    table = st.selectbox("Table", ["Person", "Hospital", "Inventory", "Supplies", "Vaccinates", "Vaccine", "Doctor"])

    if table == "Person":
        column = st.multiselect("Attribute", ["p_id","p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        column = st.multiselect("Attribute", ["h_id","h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        column = st.multiselect("Attribute", ["i_id","i_name","i_contactno","i_address"])
    elif table == "Supplies":
        column = st.multiselect("Attribute", ["s_id","s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        column = st.multiselect("Attribute", ["p","hosp","date_first","date_second"])
    elif table == "Vaccine":
        column = st.multiselect("Attribute", ["v_name","v_company","v_cost"])
    elif table == "Doctor":
        column = st.multiselect("Attribute", ["d_id","d_dept"])

    if table == "Person":
        C_attribute = st.selectbox("Condition", ["p_id","p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        C_attribute = st.selectbox("Condition", ["h_id","h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        C_attribute = st.selectbox("Condition", ["i_id","i_name","i_contactno","i_address"])
    elif table == "Supplies":
        C_attribute = st.selectbox("Condition", ["s_id","s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        C_attribute = st.selectbox("Condition", ["p","hosp","date_first","date_second"])
    elif table == "Vaccine":
        C_attribute = st.selectbox("Condition", ["v_name","v_company","v_cost"])
    elif table == "Doctor":
        C_attribute = st.selectbox("Condition", ["d_id","d_dept"])

    

    op = st.selectbox("Operator", ["=", ">", "<", ">=", "<=", "!="])

    value = st.text_input("Value")

    condition = f"{C_attribute} {op} '{value}'"

    if table == "Person":
        order_by = st.selectbox("Order By", [None,"p_id","p_name","p_contactno","p_address","p_email"])
    elif table == "Hospital":
        order_by = st.selectbox("Order By", [None,"h_id","h_name","h_pwd","h_contactno","h_type","h_address","h_email","h_vac"])
    elif table == "Inventory":
        order_by = st.selectbox("Order By", [None,"i_id","i_name","i_contactno","i_address"])
    elif table == "Supplies":
        order_by = st.selectbox("Order By", [None,"s_id","s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        order_by = st.selectbox("Order By", [None,"p","hosp","date_first","date_second"])
    elif table == "Vaccine":
        order_by = st.selectbox("Order By", [None,"v_name","v_company","v_cost"])
    elif table == "Doctor":
        order_by = st.selectbox("Order By", [None,"d_id","d_dept"])

    asc = st.selectbox("ASC order", [True, False])

    if table == "Person":
        group_by = st.selectbox("Group By", [None,"p_contactno","p_address"])
    elif table == "Hospital":
        group_by = st.selectbox("Group By", [None,"h_name","h_type","h_address","h_vac"])
    elif table == "Inventory":
        group_by = st.selectbox("Group By", [None,"i_name","i_address"])
    elif table == "Supplies":
        group_by = st.selectbox("Group By", [None,"s_hospital","s_inventory","s_quantity","s_time"])
    elif table == "Vaccinates":
        group_by = st.selectbox("Group By", [None,"hosp","date_first","date_second"])
    elif table == "Vaccine":
        group_by = st.selectbox("Group By", [None,"v_name","v_company","v_cost"])
    elif table == "Doctor":
        group_by = st.selectbox("Group By", [None,"d_dept"])
    


    if st.button("Submit"):
        f = select_function(table, column, condition, order_by,asc, group_by)
        st.write(f)
    if st.button("Back to Main Page"):
        switch_page('main')

def display_patients():
    st.title("Display Patients")
    patients = getPatients()
    if patients:
        st.write("Patients data:")
        for patient in patients:
            st.write(patient)
    else:
        st.write("No patient records found.")
    
    if st.button("Back to Main Page"):
        switch_page('main')

def display_hospitals():
    st.title("Display Hospitals")
    hospitals = getHospitals()
    if hospitals:
        st.write("Hospitals data:")
        for hospital in hospitals:
            st.write(hospital)
    else:
        st.write("No hospital records found.")

    if st.button("Back to Main Page"):
        switch_page('main')

def display_inventory():
    st.title("Display Inventory")
    inventory = getInventory()
    if inventory:
        st.write("Inventory data:")
        for item in inventory:
            st.write(item)
    else:
        st.write("No inventory records found.")

    if st.button("Back to Main Page"):
        switch_page('main')

def display_supplies():
    st.title("Display Supplies")
    patients = getSupplies()
    if patients:
        st.write("Supplies data:")
        for patient in patients:
            st.write(patient)
    else:
        st.write("No Supply records found.")
    
    if st.button("Back to Main Page"):
        switch_page('main')

def display_vaccination():
    st.title("Display Vaccination details")
    patients = getVaccination()
    if patients:
        st.write("Vaccination data:")
        for patient in patients:
            st.write(patient)
    else:
        st.write("No Vaccination records found.")
    
    if st.button("Back to Main Page"):
        switch_page('main')
    
def display_doctors():
    st.title("Display Doctors")
    doctors = getDoctors()
    if doctors:
        st.write("Doctors data:")
        for doctor in doctors:
            st.write(doctor)
    else:
        st.write("No doctor records found.")
    
    if st.button("Back to Main Page"):
        switch_page('main')

# Render pages based on the current session state
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'patients_page':
    patients_page()
elif st.session_state.page == 'hospital_page':
    insert_hospital_page()
elif st.session_state.page == 'inventory_page':
    inventory_page()
elif st.session_state.page == 'supplies_page':
    supplies_page()
elif st.session_state.page == 'vaccination_page':
    vaccination_page()
elif st.session_state.page == 'vaccine_page':
    vaccine_page()
elif st.session_state.page == 'doctor_page':
    doctor_page()
elif st.session_state.page == 'update':
    update()
elif st.session_state.page == 'delete':
    delete()
elif st.session_state.page == 'filter':
    filter()
elif st.session_state.page == 'display_patients':
    display_patients()
elif st.session_state.page == 'display_hospitals':
    display_hospitals()
elif st.session_state.page == 'display_inventory':
    display_inventory()
elif st.session_state.page == 'display_supplies':
    display_supplies()
elif st.session_state.page == 'display_vaccination':
    display_vaccination()
elif st.session_state.page == 'display_doctors':
    display_doctors()

