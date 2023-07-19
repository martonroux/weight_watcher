<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-workout-name" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <h2 style="margin-bottom: 50px">Workout Name</h2>
    <input ref="editWorkoutNameInput" class="edit-workout-name-input" type="text" v-model="input">
    <div class="align-center" style="align-self: center;">
      <Button :img-url="'close.png'" style="padding: 3px 8px 3px 8px; font-size: 24px; margin-right: 10px" @clicked="closeWindow(true)"/>
      <Button :img-url="'check_black.png'" style="padding: 5px 8px 5px 8px;" @clicked="closeWindow(false)"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      input: '',
    }
  },
  props: ['workoutName'],
  mounted() {
    this.input = this.workoutName;
    this.$refs.editWorkoutNameInput.focus();
  },
  methods: {
    closeWindow(escape) {
      if (escape === false) {
        this.$emit('close', this.input);
      } else {
        this.$emit('close', this.workoutName);
      }
    }
  }
}
</script>

<style scoped>

.edit-workout-name {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.edit-workout-name *:not(:last-child) {
  margin-bottom: 10px;
}

.edit-workout-name-input {
  font-weight: bold;
  font-size: var(--h2-font-size);
  text-transform: uppercase;
  border: none;
  outline: none;
  padding: 5px 10px;
}

.edit-workout-name *:not(:last-child) {
  margin-right: 2vw;
}

</style>