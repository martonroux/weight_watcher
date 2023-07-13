const api_link = "http://127.0.0.1:8000";


export function updateWorkout(newWorkout) {
    console.log(newWorkout['exercises']);

    for (let i = 0; i < newWorkout['exercises'].length; i++) {
        for (let j = 0; j < newWorkout['exercises'][i]['list_reps'].length; j++) {
            if (newWorkout['exercises'][i]['list_reps'][j].length === 0) {
                newWorkout['exercises'][i]['list_reps'].splice(j, 1);
                newWorkout['exercises'][i]['list_weights'].splice(j, 1);
            }
        }
    }
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
