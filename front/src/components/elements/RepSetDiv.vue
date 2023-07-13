<script setup>
import EditNbSets from "@/components/elements/edit_elems/EditNbSets.vue";
import EditNbReps from "@/components/elements/edit_elems/EditNbReps.vue";
</script>

<template>
  <div class="rep-set-div">
    <div class="rep-set-box" :class="{'tilt-shaking-anim': editActive}" @click="changeNbSets">
      <p>{{ wrktData['nb_sets'] }} sets</p>
    </div>
    <EditNbSets v-if="nbSetsEdit" :nb-sets="wrktData['nb_sets']" :index="index" @close="submitNbSets"/>
    <div class="rep-set-box" :class="{'tilt-shaking-anim': editActive}" @click="changeNbReps">
      <p>{{ wrktData['nb_reps_low'] }} - {{ wrktData['nb_reps_high'] }}</p>
    </div>
    <EditNbReps v-if="nbRepsEdit" :nb-reps-low="wrktData['nb_reps_low']" :nb-reps-high="wrktData['nb_reps_high']" :index="index" @close="submitNbReps"/>
  </div>
</template>

<script>
export default {
  data() {
    return {
      nbSetsEdit: false,
      nbRepsEdit: false
    }
  },
  props: ['wrktData', 'editActive', 'index'],
  methods: {
    changeNbSets() {
      if (this.editActive) {
        this.nbSetsEdit = true;
      }
    },
    changeNbReps() {
      if (this.editActive) {
        this.nbRepsEdit = true;
      }
    },
    submitNbSets(input, index) {
      this.nbSetsEdit = false;
      this.wrktData['nb_sets'] = input;
    },
    submitNbReps(inputLow, inputHigh, index) {
      this.nbRepsEdit = false;
      this.wrktData['nb_reps_low'] = inputLow;
      this.wrktData['nb_reps_high'] = inputHigh;
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