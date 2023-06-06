<template>
  <div class="widget">
    <h2>{{ wrktData['name'] }}</h2>
    <ol>
      <li v-for="(exercise, index) in wrktData['exercises']" :key="index">
        <div class="first-line">
          <p>
            {{ exercise['name'] }}
          </p>
          <RepSetDiv :wrkt-data="wrktData"/>
        </div>
        <WeightRepDisplay :reps-list="exercise['list_reps']" :weight-list="exercise['list_weights']"/>
      </li>
    </ol>
  </div>
</template>

<script>
import RepSetDiv from "@/components/elements/RepSetDiv.vue";
import WeightRepDisplay from "@/components/elements/weight_rep_display/WeightRepDisplay.vue";

export default {
  components: {WeightRepDisplay, RepSetDiv},
  props: ['wrktData']
}
</script>

<style scoped>

.widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
}

.widget h2 {
  color: var(--accentuation-color);
  margin-bottom: 5vw;
}

.first-line {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4vw;
}

</style>