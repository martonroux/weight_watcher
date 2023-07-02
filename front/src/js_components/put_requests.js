const api_link = "http://2.4.115.102:8000";


export function updateWorkout(newWorkout) {
    fetch(api_link + "/api/put/workout/update_workout", {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({"workout": newWorkout})
})
    .then(response => {
        if (!response.ok) {
            throw new Error("Erreur lors de la requête PUT");
        }
    })
    .catch(error => {
        console.error(error);
    });
}
