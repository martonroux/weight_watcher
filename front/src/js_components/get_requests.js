export function fetchData() {
    fetch('http://localhost:8000/api/data')
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.log("ERROR OCCURED: ", error)
        });
}

export async function fetchBodyWeights() {
    try {
        const response = await fetch('http://localhost:8000/api/get/body_weight/all_data');
        const data = await response.json();

        if (data['error'] === "False") {
            return data;
        } else {
            console.log("Error on request: ", data['error'])
            return {
                "error": true
            };
        }
    } catch (error) {
        console.log("ERROR OCCURRED: ", error);
        return {
            "error": true
        };
    }
}

export async function fetchWorkouts() {
    try {
        const response = await fetch('http://localhost:8000/api/get/workout/get_all_workouts');
        const data = await response.json();

        if (data['error'] === "False") {
            return data;
        } else {
            return NaN;
        }
    } catch (error) {
        console.log("ERROR OCCURED: ", error);
        return NaN
    }
}