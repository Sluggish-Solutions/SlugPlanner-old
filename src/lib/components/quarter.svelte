<script lang="ts">
    export let quarter_obj:any;
    let quarter_year = quarter_obj.quarter_year

    let class1= quarter_obj.data[0]
    let class2= quarter_obj.data[1]
    let class3= quarter_obj.data[2]
    
    let class4_real = false
    let class4: string;
    if (quarter_obj.data.length == 4){
        class4_real =true
        class4 = quarter_obj.data[3]
    } else{
        class4 = "lol"
    }


</script>

<div class="rounded-xl flex-grow w-auto px-1 flex flex-col items-center border bg-card text-card-foreground shadow">
    <!-- quarter_year appears on top -->
    <h1 class="text-xl font-semibold mt-2 text-center">{quarter_year}</h1>
    <!-- Rest of the content -->
    <div class=" text-center p-1">
        <a href="class/{class1}"><h1 class="p-1">{class1}</h1></a>
        <a href="class/{class2}"><h1 class="p-1">{class2}</h1></a>
        <a href="class/{class3}"><h1 class="p-1">{class3}</h1></a>
        {#if class4_real}
        <a href="class/{class4}"><h1 class="p-1">{class4}</h1></a>
        {/if}
    </div>
</div>


