<script setup>
import Button from "@/components/elements/Button.vue";
import WeightRepSingleDisplay from "@/components/elements/weight_rep_display/WeightRepSingleDisplay.vue";
import EditWeightRep from "@/components/elements/edit_elems/EditWeightRep.vue";
</script>

<template>
  <div class="weight-rep-container">
    <ol class="weight-rep-list">
      <li class="add-weight-rep" style="margin-right: 10px" v-if="editActive">
        <Button :text="'+'" style="height: 100%; border-radius: 10px; padding: 10px" @clicked="addNewData"/>
      </li>
      <li v-for="(rep, index) in repsList" :key="index">
        <div class="weight-rep-item" :class="{'weight-rep-item-active': index > 0}" :style="{cursor: editActive ? 'pointer' : 'default'}">
          <WeightRepSingleDisplay :reps-list="rep" :weight-list="weightList[index]" :edit-active="editActive" @click="changeWeightRep(rep, weightList[index])"/>
        </div>
        <EditWeightRep v-if="editWeightRep !== -1" :rep-data="repInput" :weight-data="weightInput" :index="editWeightRep" @close="handleWeightRepModif"/>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  data() {
    return {
      editWeightRep: -1,
      repInput: {},
      weightInput: {},
    }
  },
  props: ['repsList', 'weightList', 'editActive'],
  methods: {
    changeWeightRep(rep, weight, index) {
      if (this.editActive === true && this.editWeightRep === -1) {
        this.editWeightRep = index;
        this.repInput = rep;
        this.weightInput = weight;
      }
    },
    handleWeightRepModif() {
      this.editWeightRep = -1;
    },
    addNewData() {
      this.repsList.unshift([0]);
      this.weightList.unshift([0]);
    }
  }
}
</script>

<style scoped>

.weight-rep-container {
  overflow-x: scroll;
  white-space: nowrap;
  max-width: max-content;
}

.weight-rep-item {
  width: max-content;
  overflow-x: auto;
  white-space: nowrap;
}

.weight-rep-list {
  width: max-content;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.weight-rep-item-active {
  margin-left: 20px;
}

</style>