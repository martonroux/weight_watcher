import Home from "../Home.vue";
import Stats from "../Stats.vue";
import Workouts from "../Workouts.vue";

export const routes = [
    { path: '/', component: Home },
    { path: '/stats', component: Stats },
    { path: '/workouts', component: Workouts }
];
