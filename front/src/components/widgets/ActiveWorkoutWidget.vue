<script setup>
import Button from "@/components/elements/Button.vue";
import PopUpWindow from "@/components/elements/PopUpWindow.vue";
import SwitchActiveExercise from "@/components/workout/SwitchActiveExercise.vue";
</script>

<template>
  <div class="widget">
    <div class="row" style="display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
      <h2 style="color: var(--accentuation-color);">{{ workout['name'] }}</h2>
      <div class="time">
        <div class="circle">
          <div>
            <span class="minutes"></span>
            <span class="hours"></span>
          </div>
        </div>
        <p>{{ time }}</p>
      </div>
    </div>
    <div class="active-exercise">
      <div class="row" style="display: flex; flex-direction: row; justify-content: flex-end; align-items: center;">
        <h2 style="font-size: var(--body-font-size); justify-self: flex-start; margin-right: auto;">{{ activeExercise }}</h2>
        <Button style="padding: 5px 6px 3px 7px" :img-url="'swap.png'" @clicked="toggleSwitchExercise"></Button>
        <Button style="padding: 5px 6px 3px 7px" :img-url="'forward-button.png'" @clicked="forwardExercise"></Button>
      </div>
    </div>
    <div class="row" style="display: flex; flex-direction: row; margin-top: 20px; align-items: stretch; justify-content: space-between;">
      <div class="number-sets">
        <p>{{ numberSets }}</p>
      </div>
      <div class="weight-rep-modif-display" style="margin-right: 10px">
        <input ref="editRepInputRef" class="edit-weight-rep-input" type="number" inputmode="decimal" placeholder="reps" v-model="editRepInput"/>
        <input ref="editWeightInputRef" class="edit-weight-rep-input" type="number" inputmode="decimal" placeholder="kg" v-model="editWeightInput"/>
      </div>
      <Button style="padding: 5px 6px 3px 7px" :text="'Add'" @clicked="addNewWeightRep"></Button>
    </div>
    <Button :text="'End workout'" style="padding: 5px 6px 3px 7px; margin-top: 20px;" @clicked="endWorkout"/>
  </div>
  <SwitchActiveExercise v-if="switchActiveExercise" :exercises="workout['exercises']" @new-exercise="switchExercise"/>
  <PopUpWindow :open="warningPopUpOpen" ref="popup" @closed="closeWarningPopUp" style="margin: 10px">
    <p>This was the last exercise. Would you like to end the workout?</p>
  </PopUpWindow>
</template>

<script>
import {putUpdateActiveWorkout} from "@/js_components/put_requests";
import {putEndActiveWorkout} from "@/js_components/put_requests";

export default {
  data () {
    return {
      time: '',
      activeExercise: '',
      warningPopUpOpen: false,
      switchActiveExercise: false,
      numberSets: '1',
      editRepInput: '',
      editWeightInput: ''
    }
  },
  props: ['workout'],
  emits: ['endWorkout'],
  mounted() {
    this.updateTime();
  },
  watch: {
    'workout': {
      immediate: true,
      handler() {
        if (this.workout) {
          if (this.workout['act_exercise'] !== '') {
            this.activeExercise = this.workout['act_exercise'];
          } else if (this.workout['exercises'] && this.workout['exercises'].length > 0) {
            this.activeExercise = this.workout['exercises'][0]['name'];
            this.workout['act_exercise'] = this.activeExercise;
          }
          if (this.workout['exercises']) {
            for (let i = 0; i < this.workout['exercises'].length; i++) {
              if (this.workout['exercises'][i]['name'] === this.activeExercise) {
                this.numberSets = this.workout['exercises'][i]['list_reps'].length + 1;
              }
            }
          }
        }
      }
    }
  },
  methods: {
    getCurrentTime() {
      const currentTime = Date.now();
      const diff = currentTime - (this.workout['start_date'] * 1000);
      const seconds = Math.floor(diff / 1000);
      const minutes = Math.floor(seconds / 60);
      const hours = Math.floor(minutes / 60);
      const days = Math.floor(hours / 24);

      let timestamp = '';
      if (days > 0) timestamp += `${days}j `;
      if (hours > 0) timestamp += `${hours % 24}h `;
      if (minutes > 0) timestamp += `${minutes % 60}min `;
      timestamp += `${seconds % 60}s`;

      this.time = timestamp;
    },
    updateTime() {
      this.getCurrentTime();
      setTimeout(() => this.updateTime(), 1000);
    },
    closeWarningPopUp(isOk) {
      this.warningPopUpOpen = false;

      if (isOk) {
        this.endWorkout();
      }
    },
    forwardExercise() {
      const current = this.activeExercise;

      for (let i = 0; i < this.workout['exercises'].length; i++) {
        if (this.workout['exercises'][i]['name'] === current) {
          i++;
          if (i === this.workout['exercises'].length) {
            this.warningPopUpOpen = true;
          } else {
            this.activeExercise = this.workout['exercises'][i]['name'];
            this.workout['act_exercise'] = this.activeExercise;
          }
          break;
        }
      }
      for (let i = 0; i < this.workout['exercises'].length; i++) {
        if (this.workout['exercises'][i]['name'] === this.activeExercise) {
          this.numberSets = this.workout['exercises'][i]['list_reps'].length + 1;
        }
      }
      putUpdateActiveWorkout(this.workout);
    },
    toggleSwitchExercise() {
      this.switchActiveExercise = true;
    },
    switchExercise(newExercise) {
      this.switchActiveExercise = false;
      this.activeExercise = newExercise;
      this.workout['act_exercise'] = this.activeExercise;
      for (let i = 0; i < this.workout['exercises'].length; i++) {
        if (this.workout['exercises'][i]['name'] === this.activeExercise) {
          this.numberSets = this.workout['exercises'][i]['list_reps'].length + 1;
        }
      }
      putUpdateActiveWorkout(this.workout);
    },
    addNewWeightRep() {
      if (this.editRepInput === '')
        return;
      const reps = parseFloat(this.editRepInput);
      let weight = parseFloat(this.editWeightInput);

      if (this.editWeightInput === '')
        weight = 0;
      for (let i = 0; i < this.workout['exercises'].length; i++) {
        if (this.workout['exercises'][i]['name'] === this.activeExercise) {
          this.workout['exercises'][i]['list_reps'].push(reps);
          this.workout['exercises'][i]['list_weights'].push(weight);
          this.numberSets++;
          break;
        }
      }
      this.editRepInput = '';
      this.editWeightInput = '';
      putUpdateActiveWorkout(this.workout);
    },
    endWorkout() {
      putEndActiveWorkout(this.workout);
      setTimeout(() => {
        this.$emit('endWorkout');
      }, 200);
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
  display: flex;
  flex-direction: column;
}

.time {
  display: flex;
  flex-direction: row;
  align-items: center;

  .circle {
    margin-right: 10px;
  }
}

.active-exercise {
  margin-top: 20px;

  .row :not(:last-child) {
    margin-right: 10px;
  }
}

.circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: transparent;
  border: 2px solid var(--text-white);
  flex-shrink: 0;
}

.circle div {
  position: relative;
  top: 45%;
  left: -48%;
  display: flex;
  justify-content: flex-end;
  padding: 0;
}

.circle span {
  background: var(--text-white);
  height: 3px;
  border-radius: 5px;
  position: absolute;
  transition: width 0.3s;
  margin: 0;
}

.circle .minutes {
  transform-origin: 93% 50%;
  width: 42%;
  animation: rotate 10s linear infinite;
}

.circle .hours {
  transform-origin: 92% 50%;
  width: 32%;
  transform: translate(8%, 0%);
  animation: rotate 20s linear infinite;
}

.weight-rep-modif-display {
  background-color: var(--backround-color);
  border-radius: var(--widget-border-radius);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 60%;
}

.edit-weight-rep-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  background-color: transparent;
  border: none;
  outline: none;
  padding: 0 2px 0 10px;
  width: 30%;
}

.number-sets {
  height: auto;
  width: auto;
  border-radius: var(--widget-border-radius);
  border: 2px solid var(--accentuation-color);
  padding: 5px 10px 5px 10px;
  margin-right: 10px;
}

</style>