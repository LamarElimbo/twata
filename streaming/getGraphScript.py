import pickle

def getNegScript():
    
    currentScores = open('../sentimentClassifier/xScores.pkl', 'rb')
    latestScores = pickle.load(currentScores)
    currentScores.close()
    
    latestScores_ordered = sorted(list(val[1] for val in latestScores.items()))
    
    neg_latestScores_ordered = [23,12,16,20,7,29,10]
    
    def roundup (n) :
        return 10*((n+9)//10)
    
    neg_highestValue = max(neg_latestScores_ordered)

    neg_graphHeight = roundup(neg_highestValue)
    
    startNegScript = "var dataArray = " + str(neg_latestScores_ordered) + "; var graphHeight = " + str(neg_graphHeight) + "; "
    endNegScript = """
        var svg = d3.select("#neg_graph").append("svg")
                  .attr("height","500px")
                  .attr("width","100%")
                  .attr("z-index","70")
                  .attr("position", "fixed")
                  .attr("top", "0")
                  .attr("left", "0");

        svg.selectAll("rect")
            .data(dataArray)
            .enter().append("rect")
                  .attr("class", "bar")
                  .attr("height", function(d, i) {return (500*d/graphHeight)})
                  .attr("width","50")
                  .attr("z-index","80")
                  .attr("x", function(d, i) {return (i * 160) + 10})
                  .attr("y", function(d, i) {return 500 - (500*d/graphHeight)});

        svg.selectAll("text")
            .data(dataArray)
            .enter().append("text")
            .text(function(d) {return d})
                   .attr("class", "text")
                   .attr("z-index","90")
                   .attr("x", function(d, i) {return (i * 160) + 25})
                   .attr("y", function(d, i) {return 520 - (500*d/graphHeight)});
        """
    
    
    return startNegScript + endNegScript

def getPosScript():
    
    currentScores = open('../sentimentClassifier/xScores.pkl', 'rb')
    latestScores = pickle.load(currentScores)
    currentScores.close()
    
    pos_latestScores_ordered = [23,12,16,20,7,29,10]
    
    def roundup (n) :
        return 10*((n+9)//10)
    
    pos_highestValue = max(pos_latestScores_ordered)

    pos_graphHeight = roundup(pos_highestValue)
    
    startPosScript = "var dataArray = " + str(pos_latestScores_ordered) + "; var graphHeight = " + str(pos_graphHeight) + "; "
    endPosScript = """
        var svg = d3.select("#pos_graph").append("svg")
                  .attr("height","500px")
                  .attr("width","100%")
                  .attr("position", "fixed")
                  .attr("z-index","70")
                  .attr("top", "0")
                  .attr("left", "0");

        svg.selectAll("rect")
            .data(dataArray)
            .enter().append("rect")
                  .attr("class", "bar")
                  .attr("height", function(d, i) {return (500*d/graphHeight)})
                  .attr("width","50")
                  .attr("z-index","80")
                  .attr("x", function(d, i) {return (i * 160) + 10})
                  .attr("y", function(d, i) {return 500 - (500*d/graphHeight)});

        svg.selectAll("text")
            .data(dataArray)
            .enter().append("text")
            .text(function(d) {return d})
                   .attr("class", "text")
                   .attr("z-index","90")
                   .attr("x", function(d, i) {return (i * 160) + 25})
                   .attr("y", function(d, i) {return 520 - (500*d/graphHeight)});
        """
    
    return startPosScript + endPosScript
