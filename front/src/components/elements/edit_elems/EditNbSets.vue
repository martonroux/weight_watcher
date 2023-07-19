<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-nb-sets" @keyup.enter="closeWindow(false)" @keyup.esc="closeWindow(true)">
    <h2 style="margin-bottom: 50px">Number of Sets</h2>
    <input ref="editNbSetsInput" class="edit-nb-sets-input" type="number" v-model="input" inputmode="numeric">
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
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.edit-nb-sets *:not(:last-child) {
  margin-bottom: 10px;
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