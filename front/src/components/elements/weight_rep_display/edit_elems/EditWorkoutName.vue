<template>
  <div class="edit-workout-name">
    <div>
      <input ref="editWorkoutNameInput" class="edit-workout-name-input" type="text" v-model="input" @keyup.enter="closeWindow" @focusout="closeWindow">
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
    closeWindow() {
      this.$emit('close', this.input);
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
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.edit-workout-name-input {
  font-weight: bold;
  font-size: var(--h2-font-size);
  text-transform: uppercase;
  border: none;
  outline: none;
  padding: 5px 10px;
}

</style>