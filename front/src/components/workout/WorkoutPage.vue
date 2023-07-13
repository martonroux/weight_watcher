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
    </div>
    <ol>
      <li v-for="(exercise, index) in wrktData['exercises']" :key="index">
        <div class="first-line">
          <Button :img-url="'delete.png'" style="padding: 5px 7px 5px 7px; margin-right: 10px;" @clicked="openPopUp(index)" v-if="editActive"/>
          <PopUpWindow :open="popUpOpen === index" ref="popup" @closed="removeWorkout">
            <p>Are you sure?</p>
            <p>Deleting is irreversible.</p>
          </PopUpWindow>
          <p :class="{'tilt-shaking-anim': editActive}" v-if="!exerciseNameEdit" @click="changeExerciseName">
            {{ exercise['name'] }}
          </p>
          <EditExerciseName v-if="exerciseNameEdit" @close="submitExerciseName" :exercise-name="exercise['name']" :index="index"/>
          <RepSetDiv :wrkt-data="exercise" :edit-active="editActive" style="margin-left: auto;"/>
        </div>
        <WeightRepDisplay :reps-list="exercise['list_reps']" :weight-list="exercise['list_weights']" :edit-active="editActive"/>
      </li>
      <li class="add-workout" v-if="editActive">
        <Button :text="'Add Exercise'" style="padding: 5px 10px 5px 10px; border-radius: var(--widget-border-radius);" @clicked="addNewWorkout"/>
        <Button :text="'Revert changes'" style="padding: 5px 10px 5px 10px; border-radius: var(--widget-border-radius);" @clicked="openRevertChangesPopup"/>

        <PopUpWindow :open="popUpOpen === -2" ref="popup" @closed="revertChanges">
          <p>Are you sure?</p>
          <p>All current changes will be</p>
          <p>overridden.</p>
        </PopUpWindow>
      </li>
    </ol>
  </div>
</template>

<script>
import PopUpWindow from "@/components/elements/PopUpWindow.vue";


export default {
  data () {
    return {
      exerciseNameEdit: false,
      popUpOpen: -1,
    }
  },
  props: ['wrktData', 'workoutNameEdit', 'editActive'],
  emits: ['doneWorkoutEdit', 'revertChanges'],
  components: {
    PopUpWindow
  },
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
    },
    addNewWorkout() {
      const newExercise = {
        "name": "New Exercise",
        "nb_sets": 0,
        "nb_reps_low": 8,
        "nb_reps_high": 12,
        "list_weights": [],
        "list_reps": []
      }
      this.wrktData['exercises'].push(newExercise);
    },
    openPopUp(index) {
      this.popUpOpen = index;
    },
    removeWorkout(isOk) {
      if (isOk === true)
        this.wrktData['exercises'].splice(this.popUpOpen, 1);
      this.popUpOpen = -1;
    },
    openRevertChangesPopup() {
      this.popUpOpen = -2;
    },
    revertChanges(isOk) {
      this.popUpOpen = -1;
      if (isOk) {
        this.$emit('revertChanges');
      }
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
  padding-top: 30px;
  padding-bottom: 10px;
}

.widget li:not(:last-child) {
  margin: 0 0 20px 0;
}

.first-line {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 20px;
}

.add-workout {
  width: 100%;
  display: flex;
  justify-content: center;
  flex-direction: row;

  :not(:last-child) {
    margin-right: 10px;
  }
}

@media (max-width: 330px) {
  .add-workout {
    flex-direction: column;

    * {
      width: 100%;
    }

    :not(:last-child) {
      margin-bottom: 10px;
    }
  }
}

</style>