import {putNewWorkout} from "@/js_components/put_requests";

export function addWorkout(allData) {
    let idsList = [];

    for (let i = 0; i < allData.length; i++) {
        idsList.push(allData[i]['id']);
    }

    let newId;

    do {
        newId = Math.floor(Math.random() * 1000);
    } while (idsList.includes(newId));

    const newWorkout = {
        "id": newId,
        "name": "New Workout",
        "exercises": []
    }

    putNewWorkout(newWorkout);
}