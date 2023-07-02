<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-exercise-name" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <input ref="editExerciseNameInput" class="edit-exercise-name-input" type="text" v-model="input">
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
  props: ['exerciseName', 'index'],
  mounted() {
    this.input = this.exerciseName;
    this.$refs.editExerciseNameInput.focus();
  },
  methods: {
    closeWindow(escape) {
      if (escape === false) {
        const input = this.input;
        const index = this.index;

        this.$emit('close', input, index);
      } else {
        const input = this.exerciseName;
        const index = this.index;

        this.$emit('close', input, index);
      }
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
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 500px) {
  .edit-exercise-name {
    flex-direction: column;
  }

  .edit-exercise-name *:not(:last-child) {
    margin-bottom: 10px;
  }
}

.edit-exercise-name-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  border: none;
  outline: none;
  padding: 5px 10px;
}

.edit-exercise-name *:not(:last-child) {
  margin-right: 2vw;
}

</style>