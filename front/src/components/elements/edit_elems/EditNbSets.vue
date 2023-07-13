<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-nb-sets" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <h2 style="margin-bottom: 50px">Number of Sets</h2>
    <input ref="editNbSetsInput" class="edit-nb-sets-input" type="number" v-model="input" inputmode="numeric">
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
  props: ['nbSets', 'index'],
  mounted() {
    this.input = this.nbSets;
    this.$refs.editNbSetsInput.focus();
  },
  methods: {
    closeWindow(escape) {
      if (escape === false) {
        const input = this.input;
        const index = this.index;

        this.$emit('close', input, index);
      } else {
        const input = this.nbSets;
        const index = this.index;

        this.$emit('close', input, index);
      }
    }
  }
}
</script>

<style scoped>

.edit-nb-sets {
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
  .edit-nb-sets {
    flex-direction: column;
  }

  .edit-nb-sets *:not(:last-child) {
    margin-bottom: 10px;
  }
}

.edit-nb-sets-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  border: none;
  outline: none;
  padding: 5px 10px;
}

.edit-nb-sets *:not(:last-child) {
  margin-right: 2vw;
}

</style>