export function updateWorkout(newWorkout) {
    fetch("http://localhost:8000/api/put/workout/update_workout", {
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
