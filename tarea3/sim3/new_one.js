let fs = require('fs')
path = require('path')

let a1_total_prom_sum = 0
let a2_total_prom_sum = 0
let a3_total_prom_sum = 0
let a4_total_prom_sum = 0
let a5_total_prom_sum = 0
let a6_total_prom_sum = 0
let a7_total_prom_sum = 0
let a8_total_prom_sum = 0
let a9_total_prom_sum = 0
let a10_total_prom_sum = 0
let a11_total_prom_sum = 0
let a12_total_prom_sum = 0
let a13_total_prom_sum = 0
let a14_total_prom_sum = 0
let a15_total_prom_sum = 0
let a16_total_prom_sum = 0
let a17_total_prom_sum = 0
let a18_total_prom_sum = 0
let a19_total_prom_sum = 0
let a20_total_prom_sum = 0
let a21_total_prom_sum = 0
let a22_total_prom_sum = 0
let a23_total_prom_sum = 0
let a24_total_prom_sum = 0

const cliProgress = require('cli-progress');

// create a new progress bar instance and use shades_classic theme
const bar1 = new cliProgress.SingleBar({}, cliProgress.Presets.shades_classic);


const processFile = (index) => {
    filePath = path.join(__dirname, `/emails/marta-email-size.${index}.txt`);
    let data = fileread(filePath).toString();
    processData(data)

}

const fileread = (filename)  => 
{            
   var contents= fs.readFileSync(filename);
   return contents;
}    

    //Rango de horarios
    /**
     * a1 = [0-1[
     * a2 = [1-2[
     * a3 = [2-3[
     * a4 = [3-4[
     * a5 = [4-5[
     * a6 = [5-6[
     * a7 = [6-7[
     * a8 = [7-8]
     * a9 = [8-9[
     * a10 = [9-10[
     * a11= [10-11[
     * a12 = [11-12[
     * a13 = [12-13[
     * a14 = [13-14[
     * a15 = [14-15[
     * a16 = [15-16]
     * a17 = [16-17]
     * a18 = [17-18[
     * a19 = [18-19[
     * a20= [19-20[
     * a21 = [20-21[
     * a22 = [21-22[
     * a23 = [22-23[
     * a24 = [23-24[
     */
const processData = (data) => {

    let a = [
        [],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[]
    ]

    let dataSplitted = data.split(",")
    console.log("TOTAL: ", dataSplitted.length)

    

    dataSplitted.forEach((line) => {
        let lineSplit = line.split(' ')
        if(lineSplit[0] === '\n'){
            return
        }

        let time = lineSplit[0].replace('\n','')
        let size = parseInt(lineSplit[1].replace('size=',''))
        let h = parseInt(time.split(':')[0])

        //console.log("time: ", time)
        //console.log("size: ", size)
        //console.log("h: ",h)

        if(h >= 0 && h < 1){
            a[0].push(1)
        } else if( h >= 1 && h < 2){
            a[1].push(1)
        } else if(h >= 2 && h < 3){
            a[2].push(1)
        } else if(h >= 3 && h < 4){
            a[3].push(1)
        } else if(h >= 4 && h < 5){
            a[4].push(1)
        } else if(h >= 5 && h < 6){
            a[5].push(1)
        } else if(h >= 6 && h < 7){
            a[6].push(1)
        } else if(h >= 7&& h < 8){
            a[7].push(1)
        } else if( h >= 8 && h < 9){
            a[8].push(1)
        } else if(h >= 9 && h < 10){
            a[9].push(1)
        } else if(h >= 10 && h < 11){
            a[10].push(1)
        } else if(h >= 11 && h < 12){
            a[11].push(1)
        } else if(h >= 12 && h < 13){
            a[12].push(1)
        } else if(h >= 13 && h < 14){
            a[13].push(1)
        } else if(h >= 14&& h < 15){
            a[14].push(1)
        } else if( h >= 15 && h < 16){
            a[15].push(1)
        } else if(h >= 16 && h < 17){
            a[16].push(1)
        } else if(h >= 17 && h < 18){
            a[17].push(1)
        } else if(h >= 18 && h < 19){
            a[18].push(1)
        } else if(h >= 19 && h < 20){
            a[19].push(1)
        } else if(h >= 20 && h < 21){
            a[20].push(1)
        } else if(h >= 21&& h < 22){
            a[21].push(1)
        } else if(h >= 22 && h < 23){
            a[22].push(1)
        } else if(h >= 23){
            a[23].push(1)
        } 


    })

    //Final results
    //console.log("a1 is: ",a2)
    //console.log(freq(a2))
    a1_total_prom_sum += freq(a[0])
    a2_total_prom_sum += freq(a[1])
    a3_total_prom_sum += freq(a[2])
    a4_total_prom_sum += freq(a[3])
    a5_total_prom_sum += freq(a[4])
    a6_total_prom_sum += freq(a[5])
    a7_total_prom_sum += freq(a[6])
    a8_total_prom_sum += freq(a[7])
    a9_total_prom_sum += freq(a[8])
    a10_total_prom_sum += freq(a[9])
    a11_total_prom_sum += freq(a[10])
    a12_total_prom_sum += freq(a[11])
    a13_total_prom_sum += freq(a[12])
    a14_total_prom_sum += freq(a[13])
    a15_total_prom_sum += freq(a[14])
    a16_total_prom_sum += freq(a[15])
    a17_total_prom_sum += freq(a[16])
    a18_total_prom_sum += freq(a[17])
    a19_total_prom_sum += freq(a[18])
    a20_total_prom_sum += freq(a[19])
    a21_total_prom_sum += freq(a[20])
    a22_total_prom_sum += freq(a[21])
    a23_total_prom_sum += freq(a[22])
    a24_total_prom_sum += freq(a[23])


}

const freq = (arr) => {
    if(arr && arr.length > 0){
        let length = arr.length
        let freq = 0
        let debug = ""
        //let sum = arr.reduce( (s1,s2) => s1+s2,0)
        arr.forEach(s => {
            //debug+=`S is: ${s}\n`
            if(s){
                freq += s
            }
            
        })
        //let prom = Math.floor(sum/length)

        //console.log(arr)

        return freq

    } else {
        return 0
    }
    
}


const main = () => {
    // start the progress bar with a total value of 200 and start value of 0
    bar1.start(1, 0);
    let n_files = 1
    for(let i=1;i<=n_files;i++){
        processFile(i)
        bar1.update(i);
    }
    // update the current value in your application..

    

    // stop the progress bar
    bar1.stop();
   // processFile(7)
   console.log(Math.floor(a1_total_prom_sum/n_files))
   console.log(Math.floor(a2_total_prom_sum/n_files))
   console.log(Math.floor(a3_total_prom_sum/n_files))
   console.log(Math.floor(a4_total_prom_sum/n_files))
   console.log(Math.floor(a5_total_prom_sum/n_files))
   console.log(Math.floor(a6_total_prom_sum/n_files))
   console.log(Math.floor(a7_total_prom_sum/n_files))
   console.log(Math.floor(a8_total_prom_sum/n_files))
   console.log(Math.floor(a9_total_prom_sum/n_files))
   console.log(Math.floor(a10_total_prom_sum/n_files))
   console.log(Math.floor(a11_total_prom_sum/n_files))
   console.log(Math.floor(a12_total_prom_sum/n_files))
   console.log(Math.floor(a13_total_prom_sum/n_files))
   console.log(Math.floor(a14_total_prom_sum/n_files))
   console.log(Math.floor(a15_total_prom_sum/n_files))
   console.log(Math.floor(a16_total_prom_sum/n_files))
   console.log(Math.floor(a17_total_prom_sum/n_files))
   console.log(Math.floor(a18_total_prom_sum/n_files))
   console.log(Math.floor(a19_total_prom_sum/n_files))
   console.log(Math.floor(a20_total_prom_sum/n_files))
   console.log(Math.floor(a21_total_prom_sum/n_files))
   console.log(Math.floor(a22_total_prom_sum/n_files))
   console.log(Math.floor(a23_total_prom_sum/n_files))
   console.log(Math.floor(a24_total_prom_sum/n_files))
}

main()


