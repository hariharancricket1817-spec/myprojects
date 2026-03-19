async function studentRegister() {

    console.log("BUTTON CLICKED");

    let p = document.getElementById("pass").value;
    let rp = document.getElementById("repass").value;

    if (p !== rp) {
        alert("Passwords do not match!");
        return; // ✅ inside function (correct)
    }

    let data = {
        name: document.getElementById("name").value,
        reg_no: document.getElementById("reg_no").value,
        roll_no: document.getElementById("roll_no").value,
        email: document.getElementById("email").value,
        class: document.getElementById("class").value,
        degree: document.getElementById("degree").value,
        department: document.getElementById("department").value,
        hod_name: document.getElementById("hod_name").value,
        advisor_name: document.getElementById("advisor_name").value,
        phone: document.getElementById("phone").value,
        username: document.getElementById("username").value,
        password: document.getElementById("pass").value
    };

    console.log("Sending:", data);

    try {
        let res = await fetch("http://127.0.0.1:5000/register_student", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        let result = await res.json();
        alert(result.message);

    } catch (err) {
        console.error("ERROR:", err);
    }
}