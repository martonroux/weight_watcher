<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-workout-name" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <input ref="editWorkoutNameInput" class="edit-workout-name-input" type="text" v-model="input">
    <div class="button-container">
      <Button style="background-color: greenyellow" :text="'OK'" @clicked="closeWindow(false)"/>
      <Button style="background-color: orangered" :text="'UNDO'" @clicked="closeWindow(true)"/>
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
  backdrop-filter: blur(10px);
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 500px) {
  .edit-workout-name {
    flex-direction: column;
  }

  .edit-workout-name *:not(:last-child) {
    margin-bottom: 10px;
  }
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