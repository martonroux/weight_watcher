<script setup>
import RepSetDiv from "@/components/elements/RepSetDiv.vue";
import WeightRepDisplay from "@/components/elements/weight_rep_display/WeightRepDisplay.vue";
import EditWorkoutButton from "@/components/elements/weight_rep_display/EditWorkoutButton.vue";
import EditWorkoutName from "@/components/elements/weight_rep_display/edit_elems/EditWorkoutName.vue";
import EditExerciseName from "@/components/elements/weight_rep_display/edit_elems/EditExerciseName.vue";
</script>

<template>
  <div class="widget">
    <div class="workout-title">
      <h2 :class="{'tilt-shaking-anim': editActive}" @click="changeWorkoutName">{{ wrktData['name'] }}</h2>
      <EditWorkoutName v-if="workoutNameEdit" :workout-name="wrktData['name']" @close="submitWorkoutName"/>
      <EditWorkoutButton @clicked="handleEditWorkout"/>
    </div>
    <ol>
      <li v-for="(exercise, index) in wrktData['exercises']" :key="index">
        <div class="first-line">
          <p :class="{'tilt-shaking-anim': editActive}" v-if="!exerciseNameEdit" @click="changeExerciseName(index)">
            {{ exercise['name'] }}
          </p>
          <EditExerciseName v-if="exerciseNameEdit" @close="submitExerciseName" :exercise-name="exercise['name']" :index="index"/>
          <RepSetDiv :wrkt-data="exercise" :edit-active="editActive"/>
        </div>
        <WeightRepDisplay :reps-list="exercise['list_reps']" :weight-list="exercise['list_weights']"/>
      </li>
    </ol>
  </div>
</template>

<script>

import { updateWorkout } from "@/js_components/put_requests";

export default {
  data () {
    return {
      editActive: false,
      workoutNameEdit: false,
      exerciseNameEdit: false,
      workoutInput: '',
      exerciseInput: ''
    }
  },
  props: ['wrktData'],
  methods: {
    handleEditWorkout() {
      this.editActive = !this.editActive;
      if (this.editActive === false) {
        this.workoutNameEdit = false;
        updateWorkout(this.wrktData);
      }
    },
    changeWorkoutName() {
      if (this.editActive) {
        this.workoutNameEdit = true;
        this.workoutInput = this.wrktData['name'];
      }
    },
    changeExerciseName(index) {
      if (this.editActive) {
        this.exerciseNameEdit = true;
        this.exerciseInput = this.wrktData['exercises'][index]['name'];
      }
    },
    submitWorkoutName(newName) {
      this.workoutNameEdit = false;
      this.wrktData['name'] = newName;
    },
    submitExerciseName(input, index) {
      console.log(input);
      this.exerciseNameEdit = false;
      this.wrktData['exercises'][index]['name'] = input;
    }
  }
}
</script>

<style scoped>

.workout-title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
}

.widget h2 {
  color: var(--accentuation-color);
  margin-bottom: 5vw;
}

.widget img {
  width: 6vw;
  height: 6vw;
}

.first-line {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4vw;
}

</style>