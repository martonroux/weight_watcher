const api_link = "http://127.0.0.1:8000"; // TODO: PUT SERVER IP BACK


function compareDictionnaries(dict1, dict2) {
    const json1 = JSON.stringify(dict1);
    const json2 = JSON.stringify(dict2);

    return json1 === json2;
}


export function updateWorkout(newWorkout, oldWorkout) {
    if (compareDictionnaries(newWorkout, oldWorkout) === true) {
        return;
    }

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

export async function putNewWorkout(newWorkout) {
    try {
        const response = await fetch(api_link + "/api/put/workout/add_workout", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ "workout": newWorkout })
        });

        if (!response.ok) {
            throw new Error("Erreur lors de la requête PUT");
        }

        return true;
    } catch (error) {
        console.error(error);
        return false;
    }
}

export async function putDeleteWorkout(toRemove) {
    try {
        const response = await fetch(api_link + "/api/put/workout/delete_workout", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"id": toRemove["id"]})
        });

        if (!response.ok) {
            throw new Error("Erreur lors de la requête PUT");
        }

        return true;
    } catch (error) {
        console.error(error);
        return false;
    }
}

export async function putNewActiveWorkout(activeWorkout) {
    try {
        const response = await fetch(api_link + "/api/put/workout/change_active_workout", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"id": activeWorkout["id"]})
        });

        if (!response.ok) {
            throw new Error("Erreur lors de la requête PUT");
        }

        return true;
    } catch (error) {
        console.error(error);
        return false;
    }
}
