<script setup>
import EditNbSets from "@/components/elements/weight_rep_display/edit_elems/EditNbSets.vue";
</script>

<template>
  <div class="rep-set-div">
    <div class="rep-set-box" :class="{'tilt-shaking-anim': editActive}" @click="changeNbSets">
      <p>{{ wrktData['nb_sets'] }} sets</p>
    </div>
    <EditNbSets v-if="nbSetsEdit" :nb-sets="wrktData['nb_sets']" :index="index" @close="submitNbSets"/>
    <div class="rep-set-box" :class="{'tilt-shaking-anim': editActive}">
      <p>{{ wrktData['nb_reps_low'] }} - {{ wrktData['nb_reps_high'] }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nbSetsEdit: false,
    }
  },
  props: ['wrktData', 'editActive', 'index'],
  methods: {
    changeNbSets() {
      if (this.editActive) {
        this.nbSetsEdit = true;
      }
    },
    submitNbSets(input, index) {
      this.nbSetsEdit = false;
      this.wrktData['nb_sets'] = input;
    }
  }
}
</script>

<style scoped>

.rep-set-div {
  display: flex;
  flex-direction: row;
}

.rep-set-div .rep-set-box:not(:last-child) {
  margin-right: 10px;
}

.rep-set-box {
  height: auto;
  width: auto;
  border-radius: var(--widget-border-radius);
  border: 2px solid var(--accentuation-color);
  padding: 10px;
}

</style>