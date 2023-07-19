<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-exercise-name" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <h2 style="margin-bottom: 50px">Exercise Name</h2>
    <input ref="editExerciseNameInput" class="edit-exercise-name-input" type="text" v-model="input">
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
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.edit-exercise-name *:not(:last-child) {
  margin-bottom: 10px;
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