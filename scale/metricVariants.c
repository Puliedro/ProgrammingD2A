#include <stdio.h>
#include <stdlib.h>
int main(){
    char *variants[] = {"39636942454978","37609528688834","21864069136469","32634676478037","22958505197653","32038566330453","39636943503554","37930115858626","39822265155778","22958504771669","22958505001045","39822265286850","32634676609109","39636942422210","39636942520514","32833644920917","9521682371","32634676576341","39636942586050","32833685094485","32833645183061","32833644953685","9521682179","39636941340866","21864069005397","37930115596482","32833645084757","32634676052053","22958504869973","32833644789845","39636941996226","22958504935509","32634676510805","32833645051989","39636943208642","22958504706133","9521681091","37609528819906","39636941275330","32634676150357","32634676281429","9521682435","39636942258370","37609528328386","39636941897922","32833645019221","32038566068309","39822265221314","32833686437973","39636943044802"};
    int i = 0;
    size_t n = sizeof(variants)/sizeof(variants[0]);
    for (i = 0 ; i < n ; i++){
        printf("\npageUrl.keyword:*%s*", variants[i]);
    }


    return 0;
}