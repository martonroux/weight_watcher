<script setup>
import WorkoutWidget from "@/components/workout/WorkoutWidget.vue";
import AddWorkout from "@/components/workout/AddWorkout.vue";
</script>

<template>
  <div class="main-workout">
    <ol>
      <li v-for="(wrkt, index) in listWorkouts" :key="index">
        <WorkoutWidget :wrkt-data="wrkt" class="widget" @delWorkout="deleteWorkout"/>
      </li>
    </ol>
    <div class="add-workout-container">
      <AddWorkout :all-wrkts="listWorkouts" @updateData="updateData"/>
    </div>
  </div>
</template>

<script>
import { fetchWorkouts } from "@/js_components/get_requests";
import { putDeleteWorkout } from "@/js_components/put_requests";

export default {
  data () {
    return {
      listWorkouts: [],
    }
  },
  mounted () {
    fetchWorkouts().then(result => {
      this.listWorkouts = result['data'];
    });
  },
  methods: {
    updateData() {
      fetchWorkouts().then(result => {
        this.listWorkouts = result['data'];
      });
    },
    async deleteWorkout(workout) {
      const returnValue = await putDeleteWorkout(workout);

      if (returnValue === true)
        this.updateData();
    }
  }
}
</script>

<style scoped>

.main-workout {
  overflow-x: hidden;
}

.add-workout-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>