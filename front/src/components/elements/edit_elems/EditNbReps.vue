<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-nb-reps" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <h2 style="margin-bottom: 50px">Number of reps</h2>
    <h2>
      Low
    </h2>
    <input ref="editNbRepsLowInput" class="edit-nb-reps-input" type="number" v-model="repsLowInput" inputmode="numeric">
    <h2>
      High
    </h2>
    <input ref="editNbRepsHighInput" class="edit-nb-reps-input" type="number" v-model="repsHighInput" inputmode="numeric">
    <div class="align-center" style="align-self: center;">
      <Button :img-url="'close.png'" style="padding: 3px 8px 3px 8px; font-size: 24px; margin-right: 10px" @clicked="closeWindow(true)"/>
      <Button :img-url="'check_black.png'" style="padding: 5px 8px 5px 8px;" @clicked="closeWindow(false)"/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      repsLowInput: '',
      repsHighInput: ''
    }
  },
  props: ['nbRepsLow', 'nbRepsHigh', 'index'],
  mounted() {
    this.repsLowInput = this.nbRepsLow;
    this.repsHighInput = this.nbRepsHigh;
    this.$refs.editNbRepsLowInput.focus();
  },
  methods: {
    closeWindow(escape) {
      if (escape === false) {
        const inputLow = this.repsLowInput;
        const inputHigh = this.repsHighInput;
        const index = this.index;

        this.$emit('close', inputLow, inputHigh, index);
      } else {
        const inputLow = this.nbRepsLow;
        const inputHigh = this.nbRepsHigh;
        const index = this.index;

        this.$emit('close', inputLow, inputHigh, index);
      }
    }
  }
}
</script>

<style scoped>

.edit-nb-reps {
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

.edit-nb-reps *:not(:last-child) {
  margin-bottom: 10px;
}

.edit-nb-reps-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  border: none;
  outline: none;
  padding: 5px 10px;
}

.edit-nb-reps *:not(:last-child) {
  margin-right: 2vw;
}

</style>