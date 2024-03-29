<script setup>
import WorkoutPage from "@/components/workout/WorkoutPage.vue";
import EditWorkoutButton from "@/components/workout/weight_rep_display/EditWorkoutButton.vue";
</script>

<template>
  <div class="widget">
    <div class="widget-banner">
      <EditWorkoutButton @clicked="handleEditWorkout" v-if="activeDropDown && showEditButton" style="margin-right: 2vw; cursor: pointer;"/>
      <div class="workout-title" :class="{'tilt-shaking-anim': editActive}" @click="toggleWorkoutNameEdit">
        <h2>{{ wrktData['name'] }}</h2>
      </div>
      <div class="dropdown-button" @click="toggleDropDown">
        <div>
          <span class="line-1" :style="{'transform': 'rotate(' + -linesRotation + 'deg) translate(' + linesTranslationX + '%, ' + linesTranslationY + '%)', 'width': width + '%'}"></span>
          <span class="line-2" :style="{'transform': 'rotate(' + linesRotation + 'deg) translate(' + -linesTranslationX + '%, ' + linesTranslationY + '%)', 'width': width + '%'}"></span>
        </div>
      </div>
    </div>
    <WorkoutPage v-if="activeDropDown" :wrkt-data="wrktData" @editActive="toggleEditActive" :workout-name-edit="workoutNameEdit" :edit-active="editActive" @doneWorkoutEdit="submitWorkoutName" @revertChanges="revertChanges" @deleteWorkout="deleteWorkout"/>
  </div>
</template>
<script>

import {updateWorkout} from "@/js_components/put_requests";

export default {
  data () {
    return {
      activeDropDown: false,
      editActive: false,
      workoutNameEdit: false,
      showEditButton: false,
      linesRotation: 45,
      linesTranslationX: 20,
      linesTranslationY: 80,
      width: 80,
      wrktDataSave: {}
    }
  },
  props: ["wrktData"],
  emits: ['delWorkout'],
  mounted() {
    this.wrktDataSave = JSON.parse(JSON.stringify(this.wrktData));
  },
  methods: {
    handleEditWorkout() {
      this.editActive = !this.editActive;
      if (this.editActive === false) {
        updateWorkout(this.wrktData, this.wrktDataSave);
        this.wrktDataSave = JSON.parse(JSON.stringify(this.wrktData));
      }
    },
    toggleDropDown() {
      this.width = (this.width === 80) ? 100 : 80;
      this.linesTranslationY = (this.linesTranslationY === 80) ? 0 : 80;
      this.linesTranslationX = (this.linesTranslationX === 20) ? 0 : 20;
      this.activeDropDown = !this.activeDropDown;

      this.showEditButton = this.activeDropDown === true;
      if (this.activeDropDown === false && this.editActive === true)
        this.handleEditWorkout();
    },
    toggleEditActive(active) {
      this.editActive = active;
    },
    toggleWorkoutNameEdit() {
      if (this.editActive === true) {
        this.workoutNameEdit = true;
      } else {
        this.toggleDropDown();
      }
    },
    submitWorkoutName() {
      this.workoutNameEdit = false;
    },
    revertChanges() {
      const temp = JSON.parse(JSON.stringify(this.wrktDataSave));
      Object.assign(this.wrktData, temp);
    },
    deleteWorkout() {
      this.$emit('delWorkout', this.wrktData);
    }
  }
}
</script>

<style scoped>

.widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
  overflow-x: hidden;
}

.widget-banner {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

@media (min-width: 500px) {
  .widget-banner {
    justify-content: flex-end;
  }
  .dropdown-button {
    align-self: flex-end;
    margin-left: auto;
  }
}

.widget h2 {
  color: var(--accentuation-color);
}

img {
  width: var(--h2-font-size);
  height: var(--h2-font-size);
}

.dropdown-button {
  width: 30px;
  height: 30px;
  cursor: pointer;
  justify-self: flex-end;
  align-self: flex-end;
}

.dropdown-button div {
  position: relative;
  top: 40%;
  left: 5%;
}

.dropdown-button span {
  background: var(--text-white);
  width: 100%;
  height: 6px;
  border-radius: 5px;
  position: absolute;
  transform: translate(-100%, -100%);
  transition: transform 0.3s, width 0.3s;
}

</style>