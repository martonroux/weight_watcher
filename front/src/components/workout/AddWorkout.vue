<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="main-add-wrkt">
    <Button :text="'+'" style="width: 100%; padding: 5px 13px 5px 13px; font-size: var(--h2-font-size);" @clicked="addNewWorkout"/>
  </div>
</template>

<script>
import {addWorkout} from "@/js_components/operations/add_workout";

export default {
  props: ['allWrkts'],
  emits: ['updateData'],
  methods: {
    async addNewWorkout() {
      const returnValue = await addWorkout(this.allWrkts);

      if (returnValue === true)
        this.$emit('updateData');
    }
  }
}
</script>

<style scoped>

.main-add-wrkt {
  margin-top: 20px;
}

</style>