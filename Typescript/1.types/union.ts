function add(n1: number | string, n2: number | string){
    if(typeof n1 === 'number' && typeof n2 == 'number') {
        return n1 + n2;
    } else {
        return n1.toString() + n2.toString();
    }
}

