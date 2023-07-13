<script setup>
import RepSetDiv from "@/components/elements/RepSetDiv.vue";
import WeightRepDisplay from "@/components/elements/weight_rep_display/WeightRepDisplay.vue";
import EditWorkoutName from "@/components/elements/edit_elems/EditWorkoutName.vue";
import EditExerciseName from "@/components/elements/edit_elems/EditExerciseName.vue";
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="main-workout-page">
    <div class="workout-title">
      <EditWorkoutName v-if="workoutNameEdit" :workout-name="wrktData['name']" @close="submitWorkoutName"/>
      <div style="display: flex; flex-direction: row; justify-content: center; align-items: center;">
      </div>
    </div>
    <ol>
      <li v-for="(exercise, index) in wrktData['exercises']" :key="index">
        <div class="first-line">
          <p :class="{'tilt-shaking-anim': editActive}" v-if="!exerciseNameEdit" @click="changeExerciseName">
            {{ exercise['name'] }}
          </p>
          <EditExerciseName v-if="exerciseNameEdit" @close="submitExerciseName" :exercise-name="exercise['name']" :index="index"/>
          <RepSetDiv :wrkt-data="exercise" :edit-active="editActive"/>
        </div>
        <WeightRepDisplay :reps-list="exercise['list_reps']" :weight-list="exercise['list_weights']" :edit-active="editActive"/>
      </li>
      <li class="add-workout" style="width: 100%; display: flex; justify-content: center;">
        <Button :text="'+'" style="padding: 5px 10px 5px 10px;"/>
      </li>
    </ol>
  </div>
</template>

<script>

export default {
  data () {
    return {
      exerciseNameEdit: false,
    }
  },
  props: ['wrktData', 'workoutNameEdit', 'editActive'],
  emits: ['doneWorkoutEdit'],
  methods: {
    changeExerciseName() {
      if (this.editActive) {
        this.exerciseNameEdit = true;
      }
    },
    submitWorkoutName(newName) {
      this.$emit('doneWorkoutEdit');
      this.wrktData['name'] = newName;
    },
    submitExerciseName(input, index) {
      this.exerciseNameEdit = false;
      this.wrktData['exercises'][index]['name'] = input;
    }
  }
}
</script>

<style scoped>

.main-workout-page {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: column;
}

.workout-title {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding-top: 30px;
  padding-bottom: 30px;
}

.widget li:not(:last-child) {
  margin: 0 0 20px 0;
}

.first-line {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

</style>