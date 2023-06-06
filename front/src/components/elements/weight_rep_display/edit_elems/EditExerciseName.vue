<template>
  <div class="edit-exercise-name">
    <div>
      <input ref="editExerciseNameInput" class="edit-exercise-name-input" type="text" v-model="input" @keyup.enter="closeWindow" @focusout="closeWindow">
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
  props: ['exerciseName', 'index'],
  mounted() {
    this.input = this.exerciseName;
    this.$refs.editExerciseNameInput.focus();
  },
  methods: {
    closeWindow() {
      const input = this.input;
      const index = this.index;

      this.$emit('close', input, index);
    }
  }
}
</script>

<style scoped>

.edit-exercise-name {
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

.edit-exercise-name-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  border: none;
  outline: none;
  padding: 5px 10px;
}

</style>