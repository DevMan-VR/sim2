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
     * a1 = [0-3[
     * a2 = [3-6[
     * a3 = [6-9[
     * a4 = [9-12[
     * a5 = [12-15[
     * a6 = [15-18[
     * a7 = [18-21[
     * a8 = [21-23]
     */
const processData = (data) => {

    let a1 = []
    let a2 = []
    let a3 = []
    let a4 = []
    let a5 = []
    let a6 = []
    let a7 = []
    let a8 = []

    let dataSplitted = data.split(",")

    

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

        if(h >= 0 && h < 3){
            a1.push(size)
        } else if( h >= 3 && h < 6){
            a2.push(size)
        } else if(h >= 6 && h < 9){
            a3.push(size)
        } else if(h >= 9 && h < 12){
            a4.push(size)
        } else if(h >= 12 && h < 15){
            a5.push(size)
        } else if(h >= 15 && h < 18){
            a6.push(size)
        } else if(h >= 18 && h < 21){
            a7.push(size)
        } else if(h >= 21 && h <= 23){
            a8.push(size)
        }

    })

    //Final results
    //console.log("a1 is: ",a2)
    //console.log(prom(a2))
    a1_total_prom_sum += prom(a1)
    a2_total_prom_sum += prom(a2)
    a3_total_prom_sum += prom(a3)
    a4_total_prom_sum += prom(a4)
    a5_total_prom_sum += prom(a5)
    a6_total_prom_sum += prom(a6)
    a7_total_prom_sum += prom(a7)
    a8_total_prom_sum += prom(a8)

    //console.log(a1_total_prom_sum)


}

const prom = (arr) => {
    if(arr && arr.length > 0){
        let length = arr.length
        let sum = 0
        let debug = ""
        //let sum = arr.reduce( (s1,s2) => s1+s2,0)
        arr.forEach(s => {
            //debug+=`S is: ${s}\n`
            if(s){
                sum += s
            }
            
        })
        let prom = sum/length

        //console.log(arr)

        return prom

    } else {
        return 0
    }
    
}


const main = () => {
    // start the progress bar with a total value of 200 and start value of 0
    bar1.start(30, 0);
    let n_files = 30
    for(let i=1;i<=n_files;i++){
        processFile(i)
        bar1.update(i);
    }
    // update the current value in your application..


    // stop the progress bar
    bar1.stop();
   // processFile(7)
    console.log("Resultados:")
    console.log("\nA1 prom total is... ", Math.floor(a1_total_prom_sum/n_files))
    console.log("A2 prom total is... ", Math.floor(a2_total_prom_sum/n_files))
    console.log("A3 prom total is... ", Math.floor(a3_total_prom_sum/n_files))
    console.log("A4 prom total is... ", Math.floor(a4_total_prom_sum/n_files))
    console.log("A5 prom total is... ", Math.floor(a5_total_prom_sum/n_files))
    console.log("A6 prom total is... ", Math.floor(a6_total_prom_sum/n_files))
    console.log("A7 prom total is... ", Math.floor(a7_total_prom_sum/n_files))
    console.log("A8 prom total is... ", Math.floor(a8_total_prom_sum/n_files))

}

main()


