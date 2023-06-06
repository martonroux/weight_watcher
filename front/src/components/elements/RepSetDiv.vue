<template>
  <div class="rep-set-div">
    <div class="rep-set-box">
      <p>{{ wrktData['nb_sets'] }} sets</p>
    </div>
    <div class="rep-set-box">
      <p>{{ wrktData['nb_reps_low'] }} - {{ wrktData['nb_reps_high'] }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ['wrktData']
}
</script>

<style scoped>

.rep-set-div {
  display: flex;
  flex-direction: row;
}

.rep-set-div .rep-set-box:not(:last-child) {
  margin-right: 2vw;
}

.rep-set-box {
  height: auto;
  width: auto;
  border-radius: var(--widget-border-radius);
  border: 2px solid var(--accentuation-color);
  padding: 1vw;
}

</style>